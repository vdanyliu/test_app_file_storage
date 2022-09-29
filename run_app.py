import uvicorn

from file_storage.app import create_app

if __name__ == '__main__':
    uvicorn.run(create_app(), host="0.0.0.0", port=8000, debug=True)
