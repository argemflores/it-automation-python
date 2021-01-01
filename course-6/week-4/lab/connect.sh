#!/bin/bash

mv qwik*.pem keys/

mv ~/Downloads/qwik*.pem .

chmod 600 qwik*.pem

ssh -i qwik*.pem $1@$2

