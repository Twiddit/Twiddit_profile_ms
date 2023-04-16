docker build -t twiddit_profile_ms .
docker run -d -p 7777:7777 -e URL=0.0.0.0:7777 twiddit_profile_ms