#!/bin/zsh
source path/to/geant4.sh
source path/to/bdsim.sh
STEP=$1
DIR="runs/step_$STEP"
mkdir $DIR
for i in $(seq -20.0 $STEP 20.0)
    do
        sed -e "s;%OFFSET%;$i;g" models/template.gmad > models/model.gmad
        FILENAME="_step_${STEP}_offset_${i}"
        bdsim --file=models/model.gmad --outfile=$DIR/"run$FILENAME" --batch --ngenerate=100000
done
echo "====== COMPLETE ======"