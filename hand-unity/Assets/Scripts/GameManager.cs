using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI scoreText;
    [SerializeField] TimerScript timer;

    public int score = 0;

    void Start()
    {
        scoreText.text = score.ToString();
        timer.ResetTimer();
    }

    public void PlayerScored()
    {
        score++;
        scoreText.text = score.ToString();
        timer.ReduceTime();
        timer.ResetTimer();
    }

    public void GameOver()
    {
        timer.initTime = 5;
        timer.ResetTimer();
        timer.StopTimer();
        SceneManager.LoadScene(0);
    }

}
