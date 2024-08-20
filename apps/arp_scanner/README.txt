>  docker buildx build --platform linux/arm64 -t arp_scanner_arm64 . --load


# Упаковать докет в архив:

>  sudo docker save 0ac0173de058 > /home/andtokm/Temp/Docker/arp_scanner_arm64.tar


# Загрузить из ахива:

> docker load < arp_scanner_arm64.tar

> scp /home/andtokm/Temp/Docker/arp_scanner_arm64.tar root@192.168.1.5:arp_scanner_arm64.tar


# Run container:
>  sudo docker run --net=host -it --name arp_tests 0ac0173de058 /bin/bash
# >  docker run --net=host -v /dev/gpiomem:/dev/gpiomem -it --name gpio_tests2 7df476ca5abd /bin/bash
# >  docker run --net=host -v /dev/gpiomem:/dev/gpiomem -it --name gpio_tests2 7df476ca5abd /bin/bash
>  docker run --privileged  --net=host -v /dev/gpiomem:/dev/gpiomem -it --name gpio_tests3 7df476ca5abd /bin/bash






