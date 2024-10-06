
build:

	docker build --tag=buildozer -t vocab-trivia-app .


run:
	docker run --volume $(pwd):/home/user/hostcwd kivy/buildozer init





