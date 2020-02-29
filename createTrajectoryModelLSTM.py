modelType = "trajectoryMapCentersUseVelocity=0FrameStep=1SearchRadius=20"
liveTrajectoryPath = "J:\\Data\\Results\\1128\\control\90min\\" + modelType  "\\trajectoryCOMMap.mat"

deadTrajectoryPath = "J:\\Data\\Results\\1128\\32ug\\90min\\" + modelType "\\trajectoryCOMMap.mat"

saveDirectory = "H:\Data\Results\SVM_SequenceTrajectoryCOM\";

import os

try:
    os.stat(saveDirectory)
except:
    os.mkdir(saveDirectory)


load(liveTrajectoryPath);

indTraj = 1;

% indTraj2 = 1;

seqLength = 200;

dsr = 1;

dsInd = 0:dsr: seqLength;
dsInd(1) = 1;

ME = 0;

# modelSpecific = '32Dead';

modelSpecific = '112890Min'

modelName = 'model_seqLen' + str(seqLength) + 'dsr' + str(dsr) + '_' + modelSpecific + '.mat'


modelDirectory = saveDirectory + modelType  + '\\'
if ~exist(modelDirectory)
                  mkdir(modelDirectory)
                  end

                  modelPath = [modelDirectory modelName];

% modelPath = [modelDirectory 'model.mat'];

discardedLive = 0;
discardedDead = 0;
totalLive = 0;
totalDead = 0;

for w = 1:length(allCenters)

currWindow = allCenters
{w};

% nCells = length(framesMoving
{w});

nCells = length(currWindow);

for n = 1:nCells

totalLive = totalLive + 1;

currTraj = currWindow
{n};

currTraj = currTraj - currTraj(1,:);

if useMaxDist

updateTraj = 0;
indSeq = 0;
nSeq(indTraj) = 0;
bestMaxDist = 0;
bestind = 1;
currFeatures3 =[];

while size(currTraj, 1) >= seqLength
    indSeq = indSeq + 1;
    updateTraj = 1;

    currFeatures = currTraj(1:seqLength,:);

    feat = extractFeaturesFromTrajectoryCOM(currFeatures);

    maxDist = feat(3);

    currFeatures = currFeatures(dsInd,:);

    currFeatures3(:,:, indSeq) = currFeatures;

    nSeq(indTraj) = nSeq(indTraj) + 1;

    if (maxDist > bestMaxDist)
        bestMaxDist = maxDist;
    bestind = indSeq;
end

currTraj(1: seqLength,:) = [];
end

if (updateTraj)
    currFeatures = currFeatures3(:,:, bestind);
    currFeatures = currFeatures(:)';
liveFeatures(indTraj,:) = currFeatures;
indTraj = indTraj + 1;

else
discardedLive = discardedLive + 1;

end

else

while size(currTraj, 1) >= seqLength
    % if size(currTraj, 1) >= seqLength

    currFeatures = currTraj(1:seqLength,:);

    currFeatures = currFeatures(dsInd,:);

    currFeatures = currFeatures(:)';

    liveFeatures(indTraj,:) = currFeatures;
    indTraj = indTraj + 1;

    currTraj(1: seqLength,:) = [];
end

end

% while size(currTraj, 1) >= seqLength

% if size(currTraj, 1) >= seqLength

% if useOriginal
    % featOrig = currTraj(1:seqLength,:);
    % else
    % featOrig = [];
    % end
    %
    % if useDiff
        % featDiff = diff(currTraj(1:seqLength,:));
        % else
        % featDiff = [];
        % end
        %
        % featOrig = featOrig(:)';
        % featDiff = featDiff(:)';
        %
        % currFeatures = [featOrig featDiff];
        %
        % liveFeatures(indTraj,:) = currFeatures;
        % indTraj = indTraj + 1;
        %
        % currTraj(1: seqLength,:) = [];
        % end

        end

        end

        OLive = size(liveFeatures, 1);

        load(deadTrajectoryPath);

        indTraj = 1;

        for w=1:length(allCenters)

        currWindow = allCenters
        {w};

        nCells = length(framesMoving
        {w});

        for n=1:nCells

        totalDead = totalDead + 1;

        currTraj = currWindow
        {n};

        currTraj = currTraj - currTraj(1,:);

        if useMaxDist

            updateTraj = 0;
            indSeq = 0;
            nSeq(indTraj) = 0;
            bestMaxDist = 0;
            bestind = 1;
            currFeatures3 = [];

            while size(currTraj, 1) >= seqLength
                indSeq = indSeq + 1;
                updateTraj = 1;

                currFeatures = currTraj(1:seqLength,:);
                currFeatures = currFeatures(dsInd,:);

                feat = extractFeaturesFromTrajectoryCOM(currFeatures);

                maxDist = feat(3);

                currFeatures3(:,:, indSeq) = currFeatures;

                nSeq(indTraj) = nSeq(indTraj) + 1;

                if (maxDist > bestMaxDist)
                    bestMaxDist = maxDist;
                bestind = indSeq;
            end

        currTraj(1: seqLength,:) = [];
        end

        if (updateTraj)
            currFeatures = currFeatures3(:,:, bestind);
            currFeatures = currFeatures(:)';
        deadFeatures(indTraj,:) = currFeatures;
        indTraj = indTraj + 1;

        else
        discardedDead = discardedDead + 1;
        end

        else

        while size(currTraj, 1) >= seqLength
            % if size(currTraj, 1) >= seqLength

            currFeatures = currTraj(1:seqLength,:);

            currFeatures = currFeatures(dsInd,:);

            currFeatures = currFeatures(:)';

            deadFeatures(indTraj,:) = currFeatures;
            indTraj = indTraj + 1;

            currTraj(1: seqLength,:) = [];
        end

        end

        % while size(currTraj, 1) >= seqLength
            % % if size(currTraj, 1) >= seqLength
                %
            % if useOriginal
                % featOrig = currTraj(1:seqLength,:);
                % else
                % featOrig = [];
                % end
                %
                % if useDiff
                    % featDiff = diff(currTraj(1:seqLength,:));
                    % else
                    % featDiff = [];
                    % end
                    %
                    % featOrig = featOrig(:)';
                    % featDiff = featDiff(:)';
                    %
                    % currFeatures = [featOrig featDiff];
                    %
                    %
                    % deadFeatures(indTraj,:) = currFeatures;
                    % indTraj = indTraj + 1;
                    % currTraj(1: seqLength,:) = [];
                    % end

                    end

                    end

                    ODead = size(deadFeatures, 1);

                    percTrain = 75;

                    indLiveTrain = 1:floor(OLive * percTrain / 100);
                    liveFeaturesTrain = liveFeatures(indLiveTrain,:);
                    classLiveTrain = -ones(length(indLiveTrain), 1);
                    %
                    indDeadTrain = 1:floor(ODead * percTrain / 100);
                    deadFeaturesTrain = deadFeatures(indDeadTrain,:);
                    classDeadTrain = ones(length(indDeadTrain), 1);
                    %

                    dataTrain = [liveFeaturesTrain;
                    deadFeaturesTrain];
                    classTrain = [classLiveTrain;
                    classDeadTrain];

                    %
                    indLiveTest = ceil(OLive * percTrain / 100) + 1:OLive;
                    liveFeaturesTest = liveFeatures(indLiveTest,:);
                    classLiveTest = -ones(length(indLiveTest), 1);
                    %
                    indDeadTest = ceil(ODead * percTrain / 100) + 1:ODead;
                    deadFeaturesTest = deadFeatures(indDeadTest,:);
                    classDeadTest = ones(length(indDeadTest), 1);

                    try

                    svmStruct = svmtrain(dataTrain, classTrain, 'kernel_function', method);

                    model = svmStruct;

                    errorsPercLiveTrain = getResultsSVM(svmStruct, liveFeaturesTrain, classLiveTrain);
                    accuracyLiveTrain = 1 - errorsPercLiveTrain;
                    errorsPercDeadTrain = getResultsSVM(svmStruct, deadFeaturesTrain, classDeadTrain);
                    accuracyDeadTrain = 1 - errorsPercDeadTrain;

                    errorsPercLiveTest = getResultsSVM(svmStruct, liveFeaturesTest, classLiveTest);
                    accuracyLiveTest = 1 - errorsPercLiveTest;
                    errorsPercDeadTest = getResultsSVM(svmStruct, deadFeaturesTest, classDeadTest);
                    accuracyDeadTest = 1 - errorsPercDeadTest;

                    catch
                    ME

                    ME

                    model = 0;
                    accuracyLiveTrain = 0;
                    accuracyDeadTrain = 0;

                    accuracyLiveTest = 0;
                    accuracyDeadTest = 0;
                    end

                    accuracyLiveTrain
                    accuracyDeadTrain
                    accuracyTrain = (accuracyLiveTrain + accuracyDeadTrain) / 2

                    accuracyLiveTest
                    accuracyDeadTest
                    accuracyTest = (accuracyLiveTest + accuracyDeadTest) / 2

                    usedLive = totalLive - discardedLive
                    totalLive
                    percentUsedLive = usedLive / totalLive

                    usedDead = totalDead - discardedDead
                    totalDead
                    percentUsedDead = usedDead / totalDead

                    save(modelPath, 'model', 'seqLength', 'ME', 'useDiff', 'useOriginal', 'useMaxDist', 'dsr', 'dsInd')
