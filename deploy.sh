#!/bin/bash
BUILD_DIRECTORY=/tmp/temporary_directory_to_build
SRC_DIRECTORY=${HOME}/session3
DEPLOY_DIRECTORY=${HOME}/DEPLOY-$(date ‘+%Y%m%d’)

echo “BUILD THE SOFTWARE”


cd ${HOME} # cd ~
rm -rf ${BUILD_DIRECTORY}
rm -rf ${DEPLOY_DIRECTORY}
mkdir ${BUILD_DIRECTORY}
mkdir $ {DEPLOY_DIRECTORY}
cd ${BUILD_DIRECTORY}
cp ${SRC_DIRECTORY}/* .C .
cp ${SRC_DIRECTORY}/Makefile .
echo “BUILD SOFTWARE”
make foo.bin


echo “DEPLOY SOFTWARE”

cp *.bin $ {DEPLOY DIRECTORY}



echo "DEPLOY SOFTWARE on AWS"

scp -i ${HOME}/KEY_FOR_AWS/seb.pem -r ${DEPLOY_DIRECTORY} ubuntu@18.20.69.95:DEPLOY



echo "END OF DEPLOYMENT"
