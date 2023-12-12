class NotesSchema:
    all_notes = {
        "type": "object",
        "properties": {
            "success": {
                "type": "boolean"
            },
            "status": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "title": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "category": {
                            "type": "string"
                        },
                        "completed": {
                            "type": "boolean"
                        },
                        "created_at": {
                            "type": "string"
                        },
                        "updated_at": {
                            "type": "string"
                        },
                        "user_id": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "description",
                        "category",
                        "completed",
                        "created_at",
                        "updated_at",
                        "user_id"
                    ]
                }
            }
        },
        "required": [
            "success",
            "status",
            "message",
            "data"
        ]
    }