docker run --rm \
  --volumes-from data-container \
  -v $(pwd):/backup \
  -e TAR_OPTS="--verbose" \
  piscue/docker-backup backup "$(date +%F_%R).tar.xz"
