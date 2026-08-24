# API

`GET /` renders the application.

`GET /health` reports application/model status.

`POST /predict` accepts a multipart image under the `image` field and returns JSON containing `digit`, `confidence`, and `probabilities`.
