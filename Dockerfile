#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Kazu-Userbot https://github.com/ionmusic/Kazu-Userbot /home/kazuuserbot/ \
    && chmod 777 /home/kazuuserbot \
    && mkdir /home/kazuserbot/bin/

COPY ./sample_config.env ./config.env* /home/kazuuserbot/

WORKDIR /home/kazuuserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
