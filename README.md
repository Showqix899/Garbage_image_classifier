#Guide for running this backend on a local server
1. First, create a Python virtual environment: python -m venv venv (Windows) or python3 -m venv venv (Linux) 
2. Activate the virtual environment: venv\Script\activate (Windows) or source venv/bin/activate
3. git clone https://github.com/Showqix899/Garbage_image_classifier.git
4. pip install -r requirements.txt (Windows and Linux)
5. python manage.py makemigrations
6. python manage.py migrate
7. python manage.py runserver

#demo api responses
http://127.0.0.1:8000/api/upload/      (post method)

this is the reponse

```json
{
    "session_id": "b91107a4-6877-457a-8a28-985eccc198b8",
    "image_id": 9,
    "is_garbage": false
}
```

http://127.0.0.1:8000/api/images/        (get method)

this is the response


```json
[
    {
        "id": 9,
        "image": "/media/uploads/funnycat.jpeg",
        "is_garbage": false,
        "created_at": "2025-11-04T11:08:26.915260Z"
    },
    {
        "id": 8,
        "image": "/media/uploads/garbageimage-1_7MTPnnp.jpg",
        "is_garbage": true,
        "created_at": "2025-11-04T11:02:08.844965Z"
    },
    {
        "id": 7,
        "image": "/media/uploads/garbageImage2_IpLJjOm.webp",
        "is_garbage": true,
        "created_at": "2025-11-04T10:45:34.786380Z"
    },
    {
        "id": 6,
        "image": "/media/uploads/garbageImage2_5d4GRhy.webp",
        "is_garbage": true,
        "created_at": "2025-11-04T10:45:34.558120Z"
    },
    {
        "id": 5,
        "image": "/media/uploads/garbageImage2_5pUjra7.webp",
        "is_garbage": true,
        "created_at": "2025-11-04T10:45:33.078245Z"
    },
    {
        "id": 4,
        "image": "/media/uploads/garbageImage2_qdeZiLX.webp",
        "is_garbage": true,
        "created_at": "2025-11-04T10:45:31.969665Z"
    },
    {
        "id": 3,
        "image": "/media/uploads/573628755_881099120939579_5901507340848841712_n.jpg",
        "is_garbage": false,
        "created_at": "2025-11-04T10:30:07.843171Z"
    },
    {
        "id": 2,
        "image": "/media/uploads/garbageImage2.webp",
        "is_garbage": true,
        "created_at": "2025-11-04T10:29:18.299608Z"
    },
    {
        "id": 1,
        "image": "/media/uploads/garbageimage-1.jpg",
        "is_garbage": true,
        "created_at": "2025-11-04T10:28:30.417873Z"
    }
]
