import engine

game = engine.Engine()

def main():
    game.scene.push("menu")
    game.run()

if __name__ == "__main__":
	main()