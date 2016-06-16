FROM nimmis/apache-php5

MAINTAINER Michael Zhang <me@michaelz.xyz>

RUN apt-get update
RUN apt-get -y upgrade

COPY site.conf /etc/apache2/sites-available/000-default.conf
EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]