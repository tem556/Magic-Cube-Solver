import cv2

cap = cv2.VideoCapture(1)

while (True):

	# Capture frames in the video
	ret, frame = cap.read()

	# describe the type of font
	# to be used.
	font = cv2.FONT_HERSHEY_SIMPLEX

	# Use putText() method for
	# inserting text on video
	cv2.putText(frame,
	            'Faces the screen: Green',
	            (0, 50),
	            font, 1,
	            (0,0,0),
	            2)
	cv2.putText(frame,
	            'On top: Yellow',
	            (0, 100),
	            font, 1,
	            (0, 0, 0),
	            2)

	# Display the resulting frame
	cv2.imshow('video', frame)

	# creating 'q' as the quit
	# button for the video
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# release the cap object
cap.release()
# close all windows
cv2.destroyAllWindows()