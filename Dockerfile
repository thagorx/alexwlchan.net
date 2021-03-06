FROM ruby:2.6-alpine

LABEL maintainer "Alex Chan <alex@alexwlchan.net>"
LABEL description "Build image for alexwlchan.net"

COPY install_specktre.sh .
RUN ./install_specktre.sh

COPY Gemfile .
COPY Gemfile.lock .

# This is needed to avoid a segfault/shared library issue when running
# sassc-ruby inside Alpine.  See https://github.com/sass/sassc-ruby/issues/141
ENV BUNDLE_FORCE_RUBY_PLATFORM true

COPY install_jekyll.sh .
RUN ./install_jekyll.sh

RUN apk add gcompat

ENTRYPOINT ["bundle", "exec", "jekyll"]
