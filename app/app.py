from fastapi import FastAPI , HTTPException, File, UploadFile , Form , Depends
from app.schemas import PostCreate, PostResponse, UserRead , UserCreate
from app.db import create_db_and_tables,get_async_session, Post , User
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from app.images import imagekit
import shutil
import os
import tempfile
import uuid
from app.users import current_active_user, fastapi_users, auth_backend

@asynccontextmanager
async def lifespan(app:FastAPI):
    await create_db_and_tables()
    yield
    
app = FastAPI(lifespan=lifespan)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"]
) 
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),prefix="/auth",tags=["auth"]
    
)

app.include_router(
    fastapi_users.get_reset_password_router(auth_backend),prefix="/auth",tags=["auth"]
    
)
app.include_router(
    fastapi_users.get_verify_router(UserRead,UserCreate),prefix="/auth",tags=["auth"]
    
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"]
)


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...), 
    caption: str = Form(""),
    user: User = Depends(current_active_user)
    session: AsyncSession = Depends(get_async_session)
):
    temp_file_path = None

    try:
        # Create a temporary file on the server's disk
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
            shutil.copyfileobj(file.file, temp_file)
            temp_file_path = temp_file.name
       
        # Upload to ImageKit (Updated v5.0+ syntax)
        with open(temp_file_path, 'rb') as f:
            Upload_result = await run_in_threadpool(
                imagekit.files.upload,
                file=f,
                file_name=file.filename,
                use_unique_file_name=True,
                tags=["backend-upload"]
            )

        # Save the metadata to the database
        post = Post(
            user_id=user.id,
            caption=caption,
            url=Upload_result.url,
            file_type="video" if file.content_type.startswith("video") else "image",
            file_name=file.filename
        )
        session.add(post)
        await session.commit()
        await session.refresh(post)
        
        return post

    except Exception as e:
        # Now it will actually tell you WHAT went wrong!
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")
        
    finally:
        # Cleanup: Delete the temp file and close the uploaded file
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)
        file.file.close()    

@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
    user:User = Depends(current_active_user)
):
    result = await session.excute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    posts_data = []
    for post in posts:
        post_data.append(
            {
                "id":str(post.id),
                "caption":post.caption,
                "url":post.url,
                "file_type":post.file_type,
                "file_name":post.file_name,
                "created_at":post.created_at.isoformat()
                

            }
        )
    return {"posts":posts_data}  



@app.delete("/delete/{post_id}")
async def delete_post(post_id:str,session:AsyncSession = Depends(get_async_session),user:User = Depends(current_active_user))
      try:
        post_uuid = uuid.UUID(post_id)
        result = await session.execute(select(Post).where(Post.id == post_uuid))
        post = result.scalars().first()

        if not post:
            raise HTTPException(status_code=404, detail="File not Found")
        if post.user_id != user.id:
            raise HTTPException(status_code=403, detail="You are not authorized to delete this post")
        await session.delete(post)
        await session.commit()

        return {"success":True,"message":"Post deleted successfylly"}
    except Exeption as e:
        raise HTTPException(status_code=500,detail=str(e))