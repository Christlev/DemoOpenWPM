#!/usr/bin/python

from automation import CommandSequence, TaskManager

def run_custom_function(**kwargs):
	driver = kwargs['driver']
	url_title = driver.title
	print ("Title: %s" % url_title)
	return

if __name__ == "__main__":
	url_list = ["https://google.com"]

	manager_params, browser_params = TaskManager.load_default_params(1)
	manager = TaskManager.TaskManager(manager_params, browser_params)

	for URL in url_list:
		cs = CommandSequence.CommandSequence(URL)
		cs.get(sleep=10, timeout=60)
		cs.run_custom_function(run_custom_function)
		manager.execute_command_sequence(cs)

	manager.close()