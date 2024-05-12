# climate_panel_st
Panel de datos climáticos con streamlit


aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin <ECR>

docker pull <ECR>
docker run -d --name panel_clima -p 8501:8501 <ECR>
