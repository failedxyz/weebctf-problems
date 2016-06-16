FROM nimmis/apache-php5

MAINTAINER Michael Zhang <me@michaelz.xyz>

RUN apt-get update
RUN apt-get -y upgrade

COPY site.conf /etc/apache2/sites-available/000-default.conf
RUN mkdir -p /var/www/public
ADD files /var/www/public
EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]