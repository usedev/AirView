
# An element of this array (a "solution") describes a repository directory
# that will be checked out into your working copy.  Each solution may
# optionally define additional dependencies (via its DEPS file) to be
# checked out alongside the solution's directory.  A solution may also
# specify custom dependencies (via the "custom_deps" property) that
# override or augment the dependencies specified by the DEPS file.
solutions = [
  { "name"        : "src",
    "url"         : "http://src.chromium.org/svn/trunk/src@275690",
    "custom_deps" : {
      # To use the trunk of a component instead of what's in DEPS:
      #"component": "https://svnserver/component/trunk/",
      # To exclude a component from your working copy:
      #"data/really_large_component": None,
      "src/chrome/test/data" : None,
      "src/third_party/WebKit/LayoutTests": None,
      "src/chrome_frame/tools/test/reference_build/chrome": None,
      "src/chrome/tools/test/reference_build/chrome_mac": None,
      "src/chrome/tools/test/reference_build/chrome_win": None,
      "src/chrome/tools/test/reference_build/chrome_linux": None,
	  "src/third_party/hunspell_dictionaries": None,
    }
  }
]
