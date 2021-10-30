import src.lam as lam
import src.pi as pi

_fresh_c_variable_counter = 0
_fresh_d_variable_counter = 0
_fresh_u_variable_counter = 0
_fresh_v_variable_counter = 0


def generate_fresh_variable(letter: str) -> pi.VarProc:
    assert letter in {"c", "d", "u", "v"}
    global_variable_name = f"_fresh_{letter}_variable_counter"
    fresh_variable_name = f"_{letter}{globals()[global_variable_name]}"
    globals()[global_variable_name] += 1
    return pi.VarProc(fresh_variable_name)


def translate(e: lam.Expr, channel: str) -> pi.Proc:
    pass
