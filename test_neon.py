from sqlalchemy import create_engine,text

DATABASE_URL="postgresql://test_owner:npg_DwYkF3TX4rvS@ep-floral-credit-a1ew0o51-pooler.ap-southeast-1.aws.neon.tech/test?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)


with engine.connect() as conn:
    res = conn.execute(text("SELECT version();"))
    print("Neon db version; ",res.scalar())