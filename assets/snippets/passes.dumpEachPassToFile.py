#python

import modo, os.path

group = modo.Scene().item('shots')

for action in [i for i in group.itemGraph('itemGroups').forward() if i.type == lx.symbol.a_ACTIONCLIP and i.enabled]:
    print 'Activate %s...' % (action.name)
    action.actionClip.SetActive(1)

    path = lx.eval('query sceneservice scene.file ? current')
    splitpath = os.path.splitext(path)
    path = '%s_%s%s' % (splitpath[0], action.name, splitpath[1])

    print '\tExporting "%s"...' % path
    lx.eval('scene.saveAs {%s} $LXOB true' % path )

    print '\tSuccess.'
    print '\t++++'
