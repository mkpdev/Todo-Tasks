### `GET /tasks`

Returns a list of tasks.

```
> GET /tasks

< 200 OK
    {
        "id": 17,
        "subtask": [
            {
                "id": 9,
                "subsubtask": [
                    {
                        "id": 7,
                        "label": "SubSubtask203",
                        "completed": false,
                        "task": 9
                    }
                ],
                "label": "Subtask201",
                "completed": false,
                "task": 17
            },
            {
                "id": 10,
                "subsubtask": [
                    {
                        "id": 8,
                        "label": "SubSubtask203",
                        "completed": false,
                        "task": 10
                    }
                ],
                "label": "Subtask202",
                "completed": false,
                "task": 17
            }
        ],
        "label": "Task500",
        "completed": false
    }
]
```

### `POST /tasks`

Creates a new task.

```
> POST /tasks
{
  "subtask": [
    {
      "subsubtask": [
        {
          "label": "SubSubtask203",
          "completed": false
        }
      ],
      "label": "Subtask201",
      "completed": false
    },
    {
      "subsubtask": [
        {
          "label": "SubSubtask203",
          "completed": false
        }
      ],
      "label": "Subtask202",
      "completed": false
    }
  ],
  "label": "Task200",
  "completed": false
}
```

### `PUT PATCH /tasks/:id`

Updates the task of the given ID.

```
> PUT PATCH /tasks/:id
{
    "id": 14,
    "subtask": [
        {
            "id": 7,
            "subsubtask": [
                {
                    "id": 5,
                    "label": "SubSubtask203",
                    "completed": false,
                    "task": 7
                }
            ],
            "label": "Subtask201",
            "completed": false,
            "task": 14
        },
        {
            "id": 8,
            "subsubtask": [
                {
                    "id": 6,
                    "label": "SubSubtask203",
                    "completed": false,
                    "task": 8
                }
            ],
            "label": "Subtask202",
            "completed": false,
            "task": 14
        }
    ],
    "label": "Task200",
    "completed": false
}


< 404 Not Found
{ error: string }
```

### `DELETE /tasks/:id`

Deletes the task of the given ID.

```
> DELETE /tasks/:id

< 204 No Content

< 404 Not Found
{ error: string }
```
