>  docker buildx build --platform linux/arm64 -t py_gpio_img_arm64 . --load


# Упаковать докет в архив:

>  sudo docker save 7df476ca5abd > /home/andtokm/Temp/Docker/py_gpio_img_arm64.tar


# Загрузить из ахива:

> docker load < py_gpio_img_arm64.tar

> scp /home/andtokm/Temp/Docker/py_gpio_img_arm64.tar root@192.168.1.5:py_gpio_img_arm64.tar


# Run container:
>  sudo docker run --net=host -it --name gpio_tests 7df476ca5abd /bin/bash
# >  docker run --net=host -v /dev/gpiomem:/dev/gpiomem -it --name gpio_tests2 7df476ca5abd /bin/bash
# >  docker run --net=host -v /dev/gpiomem:/dev/gpiomem -it --name gpio_tests2 7df476ca5abd /bin/bash
>  docker run --privileged  --net=host -v /dev/gpiomem:/dev/gpiomem -it --name gpio_tests3 7df476ca5abd /bin/bash






