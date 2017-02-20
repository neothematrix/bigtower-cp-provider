from .main import BigTower

def autoload():
    return BigTower()

config = [{
    'name': 'bigtower',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'BigTower',
            'description': '<a href="http://bigtower.info" target="_blank">BigTower</a>',
            'wizard': True,
            'icon': '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4P/h4+f/vMfW+46s0//l5eTRAAAAAAAAAADx8ew34uXp/5Cqy//j6O76//76//z7+P/39vX/+fj3//37+P///vr/4+br+4+rzv/i5uz/5uLZPQAAAADV1dUGAAAAAPPw7Vfj5+z/orrY/7TE2vzd4uz66+3x++rt8fvc4uv6s8Ta/KK72v/k6O7/7OnjXAAAAAD///8FgICAAv///wUAAAAA9vHsN/Dw8MvX3+r/xNTp/73P5v+9z+b/xNTp/9fg7P/v7+/N6eXhOwAAAAD///8E////Af///wL///8C////BgAAAAAAAAAA//vzQvn384Tz8fGl8/Pxpff18oX79OxEAAAAAAAAAAD///8F////Af///wIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAABAAAAAgAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wH///8B////Af///wEkJCQHj4+PSaioqI2tra2vra2tsaamqI+IiIhNHBwcCf///wH///8B////Af///wH///8B////Af///wGVlZVBtra504anwP9KksP/MI3E/zGXy/9Mqtf/ibvS/7S1uNeFhYVHVVVVA////wH///8B////Af///wGmpqZhpLG++S1zsf9dj7f/orK8/8HCw//BwsP/ora//16pyf8wqtz/psHM+5SXl2lVVVUD////Af///wGioqI/prK++Slqqv+ptb//x8fH/8fHx//Hx8f/x8fH/8fHx//Hx8f/qbzE/yul2f+ows77iIiIR////wEzMzMFwMLD0SVmqf9Ffrb/YZTB/2Gcx/9kp8//kbvR/8vLy//Kysr/aLnY/4bB2P+svsb/MaLX/7u+v9ccHBwJra2xQYyiuv8CVKn/AVqy/wFgs/8BbL7/AYDQ/wKX4/+ZwdP/zs7O/wup6P9EuOf/zs7O/2KnyP+Pu9P/lpaWS8XFxYVNeqz/MWqn/wFXrP/CyM3/yMvO/42uxP8Bjt3/hbrU/9PT0/8LoOL/RbPj/9PT0/+uwMn/T57P/7a2to/Ozs6lMWei/1OAsP8BVar/cJe8/yd4v/8Vesb/DoPQ/7TI0//X19f/C5PX/0aq3P/X19f/1NXW/zOGwP/AwMCv1dXVpU98r/9sk7z/JGuz/5iwx/9mlsL/So3D/yuJz//C0dz/4eHh/y2T0v9hrNr/4eHh/93e3/9QkMP/yMjKrdbY2INylbz/W4i5/zJyt/+mvdT/qsDW/32mzP8yhMr/f63U/6LB2v83js7/VZ7U/6LA2f+cutP/c6LM/8rKyovKys4/scDR/0J7uv9AfLz/QH29/0F/wP9AgsL/TorD/0WJxv9Bisv/QYvM/0GLzP9Bicr/QYfI/7LG2f+wtLRHVVVVA+Lk5c1sk77/tMTW/8vU3v/L1N7/ztfg/+nq7P/P1+D/y9bf/8vW4P/L1uD/s8XW/22ax//d3t/RJCQkB////wHS0tI51tzj+X6gx//e5Oz/8/Pz//Pz8//z8/P/8/Pz//Pz8//z8/P/3uTr/32jyv/V3eT5urq6P////wH///8B////Ad3d3Vnb4OT5jKrL/7HG3v/g5u7/9PX1//T19f/g5u3/scbd/4yszv/a4eT5zs7OXf///wH///8B////Af///wH///8B19fXOezu7s3N2OP/qb/X/5m00f+ZtNH/qb/Y/83Y5P/p6urPxMnJPf///wH///8B////Af///wP///8D////Af///wFVVVUD1dXZPejo6IPs7Oyl6+vrpebm5oPOzs4/MzMzBf///wH///8B////Af///wEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'username',
                    'default': '',
                },
                {
                    'name': 'password',
                    'default': '',
                    'type': 'password',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 24,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]