# 🛰️ sensor4Gotify

**⭐ Love the idea? Star this repo, clone it, and give your server a voice in under five minutes!**

---

## 🚀 The Hook

Imagine your server could **talk to you**. Not with cryptic log files you have to go digging through, but with a friendly little push notification that says *"Hey, I'm alive and I've been running for 12 hours!"*, or a heads-up the moment your RAM starts climbing too high. That's exactly what **sensor4Gotify** does: it's a lightweight squad of Python sensors that watch your machine and report straight to your [Gotify](https://gotify.net/) server, so you're always in the loop without lifting a finger.

---

## 💡 Why sensor4Gotify?

Self-hosting is amazing, until you realize you have no idea what your server is up to while you're away from the terminal. sensor4Gotify solves exactly that, with a philosophy of **doing one thing and doing it well**:

- 💓 **"I'm alive!" heartbeat sensor**, get a warm little uptime message straight from your machine, in hours, so you know it's happy and running.
- 📊 **CPU & RAM watchdog**, set your own alert thresholds in a simple config file, and get pinged the instant usage crosses the line.
- 🧪 **Test sensor**, a friendly one-click way to confirm your Gotify connection works before you rely on it.
- 🧩 **Clean, modular design**, every sensor follows the same simple pattern (`patron_sensor`), so the codebase is a joy to read and extend.
- ⚙️ **Config-driven**, everything lives in one clear `config_sensor.toml` file: your Gotify server address, your app password, your alert thresholds. No digging through code required.

It's small, it's readable, and it's built to grow, a perfect companion for anyone running a home server, a Raspberry Pi, or a VPS who wants peace of mind delivered straight to their phone.

---

## 🔧 How It Works

1. **Set up your config.** Open `config_sensor.toml` and fill in your Gotify server's `ip`, `port`, and `password_app`, plus your desired CPU/RAM alert thresholds. It's just a handful of friendly key-value pairs.
2. **Run a sensor.** Each sensor is triggered with a simple command-line flag:
   ```bash
   python main.py -i_am_alive     # send a heartbeat with your uptime
   python main.py -test           # send a test notification
   python main.py -cpuANDram      # check usage and alert if thresholds are crossed
   ```
3. **Automate it.** Drop these commands into a cron job (or your favorite scheduler) and let sensor4Gotify quietly keep you posted around the clock.
4. **Enjoy the notifications.** Sit back, relax, and watch friendly alerts land straight in your Gotify app whenever something's worth knowing.

Under the hood, every sensor shares one elegant, reusable request pattern (`sensor/patron_sensor.py`), talking to Gotify's simple message API, so adding a brand-new sensor is refreshingly simple.

---

## 🤝 How You Can Help as a Dev

sensor4Gotify is young, friendly, and full of potential, there's so much exciting room to grow, and every contribution is genuinely welcome:

- 🌡️ **Build a new sensor!** Disk space, temperature, network traffic, Docker container health, the `patron_sensor` pattern makes adding one a great first contribution.
- 🧵 **Improve the config experience**, maybe validation, better defaults, or friendlier error messages.
- 📦 **Add a `requirements.txt` or packaging setup** to make installs even smoother for newcomers.
- 🧪 **Expand testing** to help the project stay rock-solid as it grows.
- 📝 **Polish the docs**, examples, cron snippets, Docker guides, anything that helps the next person get started faster.
- 💬 **Share ideas**, open an issue with a sensor idea, a feature wish, or just feedback. Every voice shapes where this project goes next!

This is a genuinely welcoming, beginner-friendly codebase (see `sensor_test.py` for the simplest possible example of a sensor), so whether it's your first pull request ever or your five-hundredth, you're going to feel right at home here.

Licensed under **AGPLv3**, free, open, and built for the community. 💚

---

## 🎉 Ready to give your server a voice?

**👉 Clone the repo, fill in your `config_sensor.toml`, run `python main.py -test`, and say hello to your first notification! Then come build a sensor with us, we'd love to have you.**
