> [!WARNING]
> You needs MongoDB installed! => [Donwload](https://www.mongodb.com/try/download/community)

# FastAPI + MongoDB CRUD (So Basic)

[![wakatime](https://wakatime.com/badge/user/af6e3d3d-e2b5-480d-a492-1fbd9614f9c5/project/a7cf2933-783c-46a8-bceb-734e7cead626.svg)](https://wakatime.com/badge/user/af6e3d3d-e2b5-480d-a492-1fbd9614f9c5/project/a7cf2933-783c-46a8-bceb-734e7cead626)

Is my try to learn FastAPI and a little of MongoDB, the APi can:

- Users CRUD -> Create, Read, Update, Delete
- Tasks CRUD -> Create, Read, Update, Delete

---

## How can you run?

### First: Create a Python Virtual Environment

> [!IMPORTANT]
> You can use [InitVenv](https://www.dev2forge.software/initvenv/)

```shell
# Create Venv
python -m venv .venv

# Activate Venv

# Windows
.venv\Scripts\activate
```

### Then: Install Dependencies

> [!IMPORTANT]
> You can use [InitVenv](https://www.dev2forge.software/initvenv/)

```shell
pip install -r requirements.txt
```

### Finally: Run The API/Server

- Just to use

```shell
uvicorn main:app
```

- To Devs

```shell
uvicorn main:app --reload --port 5000
```
