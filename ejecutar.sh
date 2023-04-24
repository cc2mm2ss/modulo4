#!/bin/bash

while true
do
	python3 ./consultar_clima.py 2> consultar_clima.err
	sleep 5
done
