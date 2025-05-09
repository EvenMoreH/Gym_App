# Port:
5044

# Docker image build command:
docker build -t gym-app-img .

# Docker image run command:
docker run -p 5044:5044 image-name-img
<!-- To run without a console use -d argument -->
docker run -d -p 5044:5044 image-name-img
hub
# Project Tree


# Tailwind
<!-- initialize tailwind config for given project -->
/home/code/tailwind/tailwindcss3 init

<!-- build tailwind.css output from specified input.css with --watch flag for rebuilding -->
/home/code/tailwind/tailwindcss3 -i "/home/code/repositories/Gym_App/app/static/css/input.css" -o "/home/code/repositories/Gym_App/app/static/css/output.css" --watch

<!-- build tailwind.css output from specified input.css with --minify flag to conserve space for docker -->
/home/code/tailwind/tailwindcss3 -i "/home/code/repositories/Gym_App/app/static/css/input.css" -o "/home/code/repositories/Gym_App/app/static/css/output.css" --minify