file1 = open('input.txt', 'r')
lines = file1.readlines()

stream = lines[0]
signalMarkerPosition = -1
messageMarkerPosition = -1

# signal marker
for x in range(4, len(stream)):
    streamBatch = stream[(x-4):x]
    if (streamBatch.count(streamBatch[0]) == 1 and 
        streamBatch.count(streamBatch[1]) == 1 and 
        streamBatch.count(streamBatch[2]) == 1 and 
        streamBatch.count(streamBatch[3]) == 1):
        signalMarkerPosition = x
        break

# message marker
for x in range(14, len(stream)):
    streamBatch = stream[(x-14):x]
    messageMarkerFound = True
    for y in streamBatch:
        if streamBatch.count(y) != 1:
            messageMarkerFound = False
            break
    if messageMarkerFound:
        messageMarkerPosition = x
        break

print(signalMarkerPosition)
print(messageMarkerPosition)