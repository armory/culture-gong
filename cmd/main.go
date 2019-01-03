package main

import (
	"gobot.io/x/gobot"
)

func main() {
	a := gobot.newGpioTestAdaptor()
	d := gobot.NewServoDriver(a, "1")
}
