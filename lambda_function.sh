mkdir lambda_function
cp -r app lambda_function/
cp -a venv/lib/python3.12/site-packages/. lambda_function
zip -r lambda_function.zip lambda_function