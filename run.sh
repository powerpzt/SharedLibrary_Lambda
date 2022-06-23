docker run --rm -v "$PWD"/task:/var/task -v "$PWD"/opt/lib:/opt/lib lambci/lambda:python3.8 lambda_function.lambda_handler
