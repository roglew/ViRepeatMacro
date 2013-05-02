import sublime_plugin


class ViRepeatLastMacro(sublime_plugin.TextCommand):
	def run(self, edit):
		print "Repeating last macro..."
		i = 0
		history = self.view.command_history(i, True)
		while (history[0] != 'vi_replay_macro' and history[0] is not None):
			history = self.view.command_history(i)
			i -= 1

		if history[0] is not None:
			char = history[1]["character"]
			self.view.run_command("vi_replay_macro", {"character": char})
