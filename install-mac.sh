#!/usr/bin/env bash


if [[ $(sysctl -n machdep.cpu.brand_string) =~ "Apple" ]]; then
    echo "Running on M1, using m1ddc..."
    git clone https://github.com/waydabber/m1ddc
    cd m1ddc
    make
    sudo cp m1ddc /usr/local/bin/
    cd ..
else
    # legacy
    echo "Running in legacy mode (Intel), using ddcctl..."
    brew install ddcctl
fi

pip3 install -r ./requirements.txt
