import src.lam as lam
import src.pi as pi

_fresh_c_variable_counter = 0
_fresh_d_variable_counter = 0
_fresh_u_variable_counter = 0
_fresh_v_variable_counter = 0


def generate_fresh_variable(letter: str) -> str:
    assert letter in {"c", "d", "u", "v"}
    global_variable_name = f"_fresh_{letter}_variable_counter"
    fresh_variable_name = f"_{letter}{globals()[global_variable_name]}"
    globals()[global_variable_name] += 1
    return fresh_variable_name


def translate(e: lam.Expr, channel: str) -> pi.Proc:
    if isinstance(e, lam.Var):
        # Translate a variable into π-calculus.
        return pi.Send(channel, e.s, pi.Parallel([]))
    elif isinstance(e, lam.Lam):
        # Translate an abstraction into π-calculus.
        u = generate_fresh_variable("u")
        return pi.Receive(e.s, channel, pi.Receive(u, channel, translate(e.e, u)))
    else:
        # Translate an application into π-calculus.
        assert isinstance(e, lam.App)
        c = generate_fresh_variable("c")
        d = generate_fresh_variable("d")
        v = generate_fresh_variable("v")
        return pi.Nu(
            c,
            pi.Nu(
                d,
                pi.Parallel(
                    [
                        translate(e.e1, c),
                        pi.Send(d, c, pi.Send(channel, c, pi.Parallel([]))),
                        pi.Replicate(pi.Receive(v, d, translate(e.e2, v))),
                    ]
                ),
            ),
        )
