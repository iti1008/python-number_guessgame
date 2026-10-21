#!/usr/bin/env python3
"""コンピューターが 1〜100 の数字を選び、ユーザーが当てる数当てゲーム。"""

import random
from typing import Dict, List, Optional


HintPack = Dict[str, List[str]]
Texts = Dict[str, object]


LANGUAGES: Dict[str, Texts] = {
    "ja": {
        "name": "日本語",
        "title": "=== 数当てゲーム ===",
        "intro": "1〜100 の数字を当ててください。",
        "prompt_guess": "予想する数字を入力してください (1〜100、終了は Enter): ",
        "not_int": "整数を入力してください。",
        "out_of_range": "1〜100 の範囲で入力してください。",
        "quit": "終了します。正解は {answer} でした。また遊ぼうね。",
        "win_first": "一発正解！？すごい、勘が鋭いね！",
        "win_fast": "やったね、正解！ {attempts} 回で当てるなんて上手いよ。",
        "win_normal": "正解！よく粘ったね。{attempts} 回で当たりました。",
        "play_again": "もう一度プレイしますか？ (y/n、言語変更は l): ",
        "thanks": "遊んでくれてありがとう！",
        "yes": {"y", "yes", "はい"},
        "hints": {
            "close_low": [
                "お、かなり近い！あと少し大きい数字だよ。",
                "熱い熱い！もうちょっと上を狙って。",
            ],
            "close_high": [
                "お、かなり近い！あと少し小さい数字だよ。",
                "熱い熱い！もうちょっと下を狙って。",
            ],
            "mid_low": [
                "まだ小さいよ。もっと大きい数字を試してみて。",
                "その調子！ただし正解は、まだ上の方だよ。",
            ],
            "mid_high": [
                "まだ大きいよ。もっと小さい数字を試してみて。",
                "いい攻めだけど、正解はまだ下の方だよ。",
            ],
            "far_low": [
                "まだまだ遠いぞ。ぐっと大きい数字を試してみて！",
                "その数字だと遠いな。大胆に上げていこう。",
            ],
            "far_high": [
                "まだまだ遠いぞ。ぐっと小さい数字を試してみて！",
                "その数字だと遠いな。大胆に下げていこう。",
            ],
            "overshoot_low": [
                "あ、通り過ぎちゃった。戻して、もっと小さい数字だよ。",
                "行き過ぎ！少し下げてみよう。",
            ],
            "overshoot_high": [
                "あ、通り過ぎちゃった。戻して、もっと大きい数字だよ。",
                "行き過ぎ！少し上げてみよう。",
            ],
            "wrong_way_low": [
                "あれ、さっきより遠ざかったよ。今度はもっと大きい数字だよ。",
                "今のは逆方向だ。上げていこう。",
            ],
            "wrong_way_high": [
                "あれ、さっきより遠ざかったよ。今度はもっと小さい数字だよ。",
                "今のは逆方向だ。下げていこう。",
            ],
        },
    },
    "en": {
        "name": "English",
        "title": "=== Number Guessing Game ===",
        "intro": "Guess the number between 1 and 100.",
        "prompt_guess": "Enter your guess (1-100, Enter to quit): ",
        "not_int": "Please enter a whole number.",
        "out_of_range": "Please enter a number from 1 to 100.",
        "quit": "Game over. The answer was {answer}. Let's play again sometime.",
        "win_first": "First try?! Amazing instinct!",
        "win_fast": "You got it! Nice work — only {attempts} guesses.",
        "win_normal": "Correct! You stuck with it and got it in {attempts} guesses.",
        "play_again": "Play again? (y/n, change language: l): ",
        "thanks": "Thanks for playing!",
        "yes": {"y", "yes"},
        "hints": {
            "close_low": [
                "So close! Try a slightly bigger number.",
                "You're hot! Aim a little higher.",
            ],
            "close_high": [
                "So close! Try a slightly smaller number.",
                "You're hot! Aim a little lower.",
            ],
            "mid_low": [
                "Still too low. Try a bigger number.",
                "Nice try! The answer is still higher.",
            ],
            "mid_high": [
                "Still too high. Try a smaller number.",
                "Good guess, but the answer is still lower.",
            ],
            "far_low": [
                "Way off. Go much higher!",
                "That's far from it. Jump up boldly.",
            ],
            "far_high": [
                "Way off. Go much lower!",
                "That's far from it. Jump down boldly.",
            ],
            "overshoot_low": [
                "You passed it! Come back to a smaller number.",
                "Too far! Come down a bit.",
            ],
            "overshoot_high": [
                "You passed it! Come back to a bigger number.",
                "Too far! Come up a bit.",
            ],
            "wrong_way_low": [
                "You moved farther away. Go higher this time.",
                "That's the wrong direction. Go up.",
            ],
            "wrong_way_high": [
                "You moved farther away. Go lower this time.",
                "That's the wrong direction. Go down.",
            ],
        },
    },
    "zh": {
        "name": "中文",
        "title": "=== 猜数字游戏 ===",
        "intro": "请猜 1 到 100 之间的数字。",
        "prompt_guess": "请输入你的猜测（1〜100，直接按 Enter 结束）: ",
        "not_int": "请输入整数。",
        "out_of_range": "请输入 1 到 100 之间的数字。",
        "quit": "结束了。正确答案是 {answer}。下次再玩吧。",
        "win_first": "一次就猜中？！直觉太准了！",
        "win_fast": "答对了！只用了 {attempts} 次，真厉害。",
        "win_normal": "答对了！坚持得很好，一共 {attempts} 次。",
        "play_again": "再玩一次吗？(y/n，切换语言请输入 l): ",
        "thanks": "谢谢你来玩！",
        "yes": {"y", "yes", "是", "好"},
        "hints": {
            "close_low": [
                "很接近了！再大一点点。",
                "很热！再往上一点。",
            ],
            "close_high": [
                "很接近了！再小一点点。",
                "很热！再往下一点。",
            ],
            "mid_low": [
                "还是偏小。试试更大的数字。",
                "不错！答案还在上面。",
            ],
            "mid_high": [
                "还是偏大。试试更小的数字。",
                "猜得不错，但答案还在下面。",
            ],
            "far_low": [
                "还差得远。大胆往大了猜！",
                "离得有点远，往上跨一大步吧。",
            ],
            "far_high": [
                "还差得远。大胆往小了猜！",
                "离得有点远，往下跨一大步吧。",
            ],
            "overshoot_low": [
                "走过头了！回来，再小一点。",
                "过了！稍微往下调。",
            ],
            "overshoot_high": [
                "走过头了！回来，再大一点。",
                "过了！稍微往上调。",
            ],
            "wrong_way_low": [
                "比刚才更远了。这次往大了猜。",
                "方向反了，往上走。",
            ],
            "wrong_way_high": [
                "比刚才更远了。这次往小了猜。",
                "方向反了，往下走。",
            ],
        },
    },
    "ko": {
        "name": "한국어",
        "title": "=== 숫자 맞히기 게임 ===",
        "intro": "1부터 100 사이의 숫자를 맞춰 보세요.",
        "prompt_guess": "숫자를 입력하세요 (1〜100, 종료는 Enter): ",
        "not_int": "정수를 입력해 주세요.",
        "out_of_range": "1부터 100 사이의 숫자를 입력해 주세요.",
        "quit": "종료합니다. 정답은 {answer}이었어요. 또 놀아요.",
        "win_first": "한 번에 맞혔다고?! 감이 대단해요!",
        "win_fast": "정답! {attempts}번 만에 맞히다니 잘하네요.",
        "win_normal": "정답! 잘 버텼어요. {attempts}번 만에 맞혔습니다.",
        "play_again": "한 판 더 할까요? (y/n, 언어 변경은 l): ",
        "thanks": "놀아 줘서 고마워요!",
        "yes": {"y", "yes", "네", "ㅇ"},
        "hints": {
            "close_low": [
                "오, 꽤 가까워요! 조금만 더 큰 숫자요.",
                "뜨거워요! 살짝 위를 노려 보세요.",
            ],
            "close_high": [
                "오, 꽤 가까워요! 조금만 더 작은 숫자요.",
                "뜨거워요! 살짝 아래를 노려 보세요.",
            ],
            "mid_low": [
                "아직 작아요. 더 큰 숫자를 시도해 보세요.",
                "좋아요! 정답은 아직 위쪽이에요.",
            ],
            "mid_high": [
                "아직 커요. 더 작은 숫자를 시도해 보세요.",
                "좋은 시도지만, 정답은 아직 아래쪽이에요.",
            ],
            "far_low": [
                "아직 멀어요. 훨씬 큰 숫자를 해보세요!",
                "꽤 멀어요. 과감하게 올려 봐요.",
            ],
            "far_high": [
                "아직 멀어요. 훨씬 작은 숫자를 해보세요!",
                "꽤 멀어요. 과감하게 내려 봐요.",
            ],
            "overshoot_low": [
                "아, 지나쳤어요. 돌아와서 더 작은 숫자요.",
                "너무 갔어요! 조금 낮춰 봐요.",
            ],
            "overshoot_high": [
                "아, 지나쳤어요. 돌아와서 더 큰 숫자요.",
                "너무 갔어요! 조금 높여 봐요.",
            ],
            "wrong_way_low": [
                "아까보다 멀어졌어요. 이번엔 더 큰 숫자요.",
                "반대 방향이에요. 올려 봐요.",
            ],
            "wrong_way_high": [
                "아까보다 멀어졌어요. 이번엔 더 작은 숫자요.",
                "반대 방향이에요. 내려 봐요.",
            ],
        },
    },
    "es": {
        "name": "Español",
        "title": "=== Adivina el número ===",
        "intro": "Adivina el número entre 1 y 100.",
        "prompt_guess": "Escribe tu número (1-100, Enter para salir): ",
        "not_int": "Introduce un número entero.",
        "out_of_range": "Introduce un número del 1 al 100.",
        "quit": "Fin del juego. La respuesta era {answer}. Volvamos a jugar otro día.",
        "win_first": "¿A la primera? ¡Qué instinto!",
        "win_fast": "¡Correcto! Muy bien, solo {attempts} intentos.",
        "win_normal": "¡Correcto! Lo lograste en {attempts} intentos.",
        "play_again": "¿Otra partida? (y/n, cambiar idioma: l): ",
        "thanks": "¡Gracias por jugar!",
        "yes": {"y", "yes", "s", "si", "sí"},
        "hints": {
            "close_low": [
                "¡Muy cerca! Prueba un número un poco más grande.",
                "¡Caliente! Apunta un poco más arriba.",
            ],
            "close_high": [
                "¡Muy cerca! Prueba un número un poco más pequeño.",
                "¡Caliente! Apunta un poco más abajo.",
            ],
            "mid_low": [
                "Todavía es bajo. Prueba un número más grande.",
                "¡Bien! La respuesta sigue más arriba.",
            ],
            "mid_high": [
                "Todavía es alto. Prueba un número más pequeño.",
                "Buena idea, pero la respuesta sigue más abajo.",
            ],
            "far_low": [
                "Está lejos. ¡Sube bastante!",
                "Queda lejos. Sube con valentía.",
            ],
            "far_high": [
                "Está lejos. ¡Baja bastante!",
                "Queda lejos. Baja con valentía.",
            ],
            "overshoot_low": [
                "¡Te pasaste! Vuelve a un número más pequeño.",
                "¡Demasiado lejos! Baja un poco.",
            ],
            "overshoot_high": [
                "¡Te pasaste! Vuelve a un número más grande.",
                "¡Demasiado lejos! Sube un poco.",
            ],
            "wrong_way_low": [
                "Te alejaste. Esta vez ve más arriba.",
                "Dirección contraria. Sube.",
            ],
            "wrong_way_high": [
                "Te alejaste. Esta vez ve más abajo.",
                "Dirección contraria. Baja.",
            ],
        },
    },
}

LANG_ORDER = ["ja", "en", "zh", "ko", "es"]
CHANGE_LANG = {"l", "lang", "language", "言語"}


def choose_language() -> Texts:
    print("=== Number Guessing Game / 数当てゲーム ===")
    print("Choose a language / 言語を選んでください:")
    for index, code in enumerate(LANG_ORDER, start=1):
        print(f"  {index}) {LANGUAGES[code]['name']} ({code})")

    while True:
        raw = input("> ").strip().lower()
        if raw.isdigit():
            choice = int(raw)
            if 1 <= choice <= len(LANG_ORDER):
                return LANGUAGES[LANG_ORDER[choice - 1]]
        if raw in LANGUAGES:
            return LANGUAGES[raw]
        print("Please choose 1-5 or ja/en/zh/ko/es")


def read_guess(texts: Texts) -> Optional[int]:
    raw = input(str(texts["prompt_guess"])).strip()
    if raw == "":
        return None
    try:
        guess = int(raw)
    except ValueError:
        print(texts["not_int"])
        return read_guess(texts)
    if guess < 1 or guess > 100:
        print(texts["out_of_range"])
        return read_guess(texts)
    return guess


def hint_for(
    guess: int,
    answer: int,
    hints: HintPack,
    previous: Optional[int] = None,
) -> str:
    gap = abs(answer - guess)
    too_low = guess < answer
    overshot = False
    wrong_way = False
    if previous is not None:
        prev_gap = abs(answer - previous)
        overshot = (previous < answer < guess) or (guess < answer < previous)
        wrong_way = (not overshot) and gap > prev_gap

    if overshot:
        key = "overshoot_high" if too_low else "overshoot_low"
    elif wrong_way:
        key = "wrong_way_low" if too_low else "wrong_way_high"
    elif gap <= 5:
        key = "close_low" if too_low else "close_high"
    elif gap >= 30:
        key = "far_low" if too_low else "far_high"
    else:
        key = "mid_low" if too_low else "mid_high"
    return random.choice(hints[key])


def play_round(texts: Texts) -> None:
    answer = random.randint(1, 100)
    attempts = 0
    previous = None
    hints = texts["hints"]
    print("\n" + str(texts["intro"]))

    while True:
        guess = read_guess(texts)
        if guess is None:
            print(str(texts["quit"]).format(answer=answer))
            return

        attempts += 1
        if guess != answer:
            print(hint_for(guess, answer, hints, previous))
            previous = guess
            continue
        if attempts == 1:
            print(texts["win_first"])
        elif attempts <= 5:
            print(str(texts["win_fast"]).format(attempts=attempts))
        else:
            print(str(texts["win_normal"]).format(attempts=attempts))
        return


def main() -> None:
    texts = choose_language()
    print(texts["title"])
    while True:
        play_round(texts)
        again = input(str(texts["play_again"])).strip().lower()
        if again in CHANGE_LANG:
            texts = choose_language()
            print(texts["title"])
            continue
        if again not in texts["yes"]:
            print(texts["thanks"])
            break


if __name__ == "__main__":
    main()
