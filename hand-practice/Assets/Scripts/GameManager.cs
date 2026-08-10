using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI scoreText;
    [SerializeField] TextMeshProUGUI timerText; 
    [SerializeField] TimerScript timer;

    int score = 0;

    void Start()
    {
        scoreText.text = score.ToString();
        timer.ResetTimer();
    }

    public void PlayerScored()
    {
        score++;
        scoreText.text = score.ToString();
        timer.ResetTimer();
    }

    public void GameOver()
    {
        timer.ResetTimer();
        timer.StopTimer();
        SceneManager.LoadScene(0);
    }

}
