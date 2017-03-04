import os
from flask import Flask

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True,
)

# controllers
@app.route("/")
def counter(min, max):
	def count: for num in range(min, max):
		return num


	for x in range(0, 1000):
		if x < 5:
			print 'x = ', x
			for y in range(0, 10000):
				if y < 5:
					print 'y = ', y

					counter(x, y)

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)