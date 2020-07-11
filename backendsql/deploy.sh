sudo docker build -t littlemall/littlemallfe-service .
sudo docker run --name littlemallfeservice -p 7106:7106 -d littlemall/littlemallfe-service