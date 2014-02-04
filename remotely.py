import sublime
import sublime_plugin
import os


def get_filepath_settings(view, string):
  remotely_filepaths = view.settings().get(string)
  return remotely_filepaths


class Remotely(sublime_plugin.EventListener):
  def on_post_save(self, view):
    remotely_filepaths = get_filepath_settings(view, 'remotely_filepaths')

    for dirname, target in remotely_filepaths.items():
      if view.file_name().startswith(dirname):
        target = target.replace("$1", view.file_name())
        target = target.replace("$2", view.file_name()[len(dirname):])

        os.system(target + " &")
