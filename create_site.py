#!/usr/bin/env python
# __NO_RELICENSE__

import os, random, subprocess, sys

CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
BLACKLIST = (
    '.tar.gz',
    '/.git/',
    '.svn',
    '.hg',
)

def replace(repl, text):
    text = text.replace('/gitignore', '/.gitignore')
    for key, value in repl.iteritems():
        text = text.replace('$$$$%s$$$$' % (key,), value)
    return text

def gen_secret():
    """ Generate a site key in the same manner Django does for the settings in
    the example app. Shamelessly copied from startproject.py in the django 
    source. """
    return ''.join([random.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

def main(repl, dest, templ_dir):
    try:
        os.makedirs(dest)
    except OSError:
        pass
    
    for root, dirs, files in os.walk(templ_dir):
        for filename in files:
            source_fn = os.path.join(root, filename)
            dest_fn = replace(repl, os.path.join(dest, root.replace(templ_dir, ''), replace(repl, filename)))
            try:
                os.makedirs(os.path.dirname(dest_fn))
            except OSError:
                pass
            print 'Copying %s to %s' % (source_fn, dest_fn)
            should_replace = True
            for bl_item in BLACKLIST:
                if bl_item in dest_fn:
                    should_replace = False
            data = open(source_fn, 'r').read()
            if should_replace:
                data = replace(repl, data)
            open(dest_fn, 'w').write(data)
            os.chmod(dest_fn, os.stat(source_fn)[0])

    if repl['VIRTENV'] == 'NONE':
        print "Skipping the virtual environment setup."
        return
    
    HAS_VENV = bool(subprocess.Popen(['which','virtualenv'], stdout=subprocess.PIPE).communicate()[0])
    if not HAS_VENV:
        print "can't install a virtualenv environment. Please install virtualenv with\n  easy_install virtualenv\n\nor\n\n  pip virtualenv"
        sys.exit(1)

    HAS_VENVW = bool(subprocess.Popen(['which','virtualenvwrapper.sh'], stdout=subprocess.PIPE).communicate()[0])
    if not HAS_VENVW:
        print "can't install a virtualenvwrapper environment.  Please install virtualenvwrapper with\n  easy_install virtualenvwrapper\n\nor\n\n  pip virtualenvwrapper"
        sys.exit(1)

    print "Making the virtual environment (%s)..." % repl['VIRTENV']
    create_env_cmds = [
        'source virtualenvwrapper.sh', 
        'cd %s' % dest,
        'mkvirtualenv --no-site-packages --distribute %s' % repl['VIRTENV'],
        'easy_install pip'
        ]
    create_pa_cmd = [
        'source virtualenvwrapper.sh',
        'cat > $WORKON_HOME/%s/bin/postactivate '\
        '<<END\n#!/bin/bash/\ncd %s\nEND\n'\
        'chmod +x $WORKON_HOME/%s/bin/postactivate' % (repl['VIRTENV'], dest,repl['VIRTENV'])
        ]
    subprocess.call([';'.join(create_env_cmds)], env=os.environ, executable='/bin/bash', shell=True)
    subprocess.call([';'.join(create_pa_cmd)], env=os.environ, executable='/bin/bash', shell=True)
    
    print "Now type: workon %s" % repl['VIRTENV']

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--author", dest="author", help="The name of the author.")
    parser.add_option("-n", "--name", dest="site_name", help="The name of the site, like 'geocamAwesome'.")
    parser.add_option("-v", "--VIRTENV", dest="VIRTENV", help="The name of the virtualenv.")
    parser.add_option("-d", "--dest", dest="destination", help="Where to put the new site. Relative paths are recognized.")
    parser.add_option("-t", "--template", dest="template", help="The template to use as a basis for the new site.", default=os.path.abspath(os.path.join(os.path.dirname(__file__), 'skel')))
    parser.add_option('--use-virtenv', dest='use_virtenv', action='store_true', default=False, help="Use a virtual env")
    (options, args) = parser.parse_args()
    
    repl = {
        'SITE_NAME': None,
        'AUTHOR': None,
        'SITE_SECRET': gen_secret()
    }
    dest_dir = None
    templ_dir = None
    
    cur_user = os.getlogin()
    
    if options.site_name:
        repl['SITE_NAME'] = options.site_name
    elif len(args) > 0:
        repl['SITE_NAME'] = args[0]
    
    while not repl['SITE_NAME']:
        repl['SITE_NAME'] = raw_input('Site name: ')
    
    if options.author:
        repl['AUTHOR'] = options.author
    while not repl['AUTHOR']:
        repl['AUTHOR'] = raw_input('Author [%s]: ' % cur_user) or cur_user
    
    repl['SECRET_KEY'] = ''.join([random.choice(CHARS) for i in xrange(50)])
    
    if options.destination:
        dest_dir = options.destination
    
    while not dest_dir:
        dest_dir = raw_input('Destination directory [%s]: ' % (os.getcwd(),)) or os.getcwd()
    dest_dir =  os.path.realpath(os.path.expanduser(dest_dir))
    dest = os.path.join(dest_dir, repl['SITE_NAME'])

    if options.template:
        templ_dir = options.template

    default = os.path.abspath(os.path.join(os.path.dirname(__file__), 'skel'))
    while not templ_dir:
        templ_dir = raw_input('Site template directory [%s]: ' % default) or default
    templ_dir = os.path.realpath(os.path.expanduser(templ_dir))
    if templ_dir[-1] != '/':
        templ_dir = templ_dir + "/"
    
    if options.VIRTENV:
        repl['VIRTENV'] = options.VIRTENV
    else:
        repl['VIRTENV'] = None

    if not options.use_virtenv and not repl['VIRTENV']:
        repl['VIRTENV'] = 'NONE'
    else:
        while not repl['VIRTENV']:
            repl['VIRTENV'] = raw_input('Virtual environment name [%s]: ' % repl['SITE_NAME']) or repl['SITE_NAME']

    main(repl, dest, templ_dir)
