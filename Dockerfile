#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Kazu-Userbot https://github.com/ionmusic/Kazu-Userbot /home/Kazuuserbot/ \
    && chmod 777 /home/Kazuuserbot \
    && mkdir /home/Kazuuserbot/bin/

COPY ./sample_config.env ./config.env* /home/Kazuuserbot/

WORKDIR /home/Kazuuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
