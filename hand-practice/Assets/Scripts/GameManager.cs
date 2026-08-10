using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI scoreText;
    [SerializeField] TextMeshProUGUI timerText;
    [SerializeField] GameObject timer;

    int score = 0;

    void Start()
    {
        scoreText.text = score.ToString();
    }

    public void PlayerScored()
    {
        score++;
        scoreText.text = score.ToString();
    }

    public void GameOver()
    {
        SceneManager.LoadScene(0);
    }

}
