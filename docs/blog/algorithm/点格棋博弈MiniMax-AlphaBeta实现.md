---
title: 点格棋博弈MiniMax-AlphaBeta实现
date: 2025-10-11
category: 博弈论
tags:
  - 算法
outline: deep
---

- 1- 我来为你实现一个完整的点格棋博弈程序，包含棋面表示和MiniMax算法。
- ## 完整代码实现
	  
	  ```cpp
	  #include 
	  #include 
	  #include 
	  #include 
	  #include 
	  
	  // 点格棋游戏类
	  class DotsAndBoxes {
	  private:
	    int size; // 棋盘大小 (size x size 个格子)
	    std::vector> horizontalLines; // 水平线
	    std::vector> verticalLines;   // 垂直线
	    std::vector> boxes;           // 格子归属 (0: 未完成, 1: 玩家1, 2: 玩家2)
	    int currentPlayer; // 当前玩家 (1 或 2)
	    int player1Score, player2Score;
	  
	  public:
	    // 构造函数
	    DotsAndBoxes(int n) : size(n), currentPlayer(1), player1Score(0), player2Score(0) {
	        // 初始化棋盘
	        horizontalLines.resize(size + 1, std::vector(size, false));
	        verticalLines.resize(size, std::vector(size + 1, false));
	        boxes.resize(size, std::vector(size, 0));
	    }
	  
	    // 复制构造函数
	    DotsAndBoxes(const DotsAndBoxes& other) {
	        size = other.size;
	        currentPlayer = other.currentPlayer;
	        player1Score = other.player1Score;
	        player2Score = other.player2Score;
	        horizontalLines = other.horizontalLines;
	        verticalLines = other.verticalLines;
	        boxes = other.boxes;
	    }
	  
	    // 检查游戏是否结束
	    bool isGameOver() const {
	        return player1Score + player2Score == size * size;
	    }
	  
	    // 获取当前玩家
	    int getCurrentPlayer() const {
	        return currentPlayer;
	    }
	  
	    // 获取玩家分数
	    std::pair getScores() const {
	        return {player1Score, player2Score};
	    }
	  
	    // 获取赢家 (0: 平局, 1: 玩家1, 2: 玩家2)
	    int getWinner() const {
	        if (!isGameOver()) return 0;
	        if (player1Score > player2Score) return 1;
	        if (player2Score > player1Score) return 2;
	        return 0; // 平局
	    }
	  
	    // 检查移动是否合法
	    bool isValidMove(int type, int row, int col) const {
	        if (type == 0) { // 水平线
	            return row >= 0 && row = 0 && col = 0 && row = 0 && col >> getValidMoves() const {
	        std::vector>> moves;
	        
	        // 水平线移动
	        for (int i = 0; i  0) {
	                if (horizontalLines[row-1][col] && verticalLines[row-1][col] && verticalLines[row-1][col+1]) {
	                    boxes[row-1][col] = currentPlayer;
	                    completedBoxes++;
	                    if (currentPlayer == 1) player1Score++;
	                    else player2Score++;
	                }
	            }
	            
	            // 检查下方的格子
	            if (row  0) {
	                if (verticalLines[row][col-1] && horizontalLines[row][col-1] && horizontalLines[row+1][col-1]) {
	                    boxes[row][col-1] = currentPlayer;
	                    completedBoxes++;
	                    if (currentPlayer == 1) player1Score++;
	                    else player2Score++;
	                }
	            }
	            
	            // 检查右侧的格子
	            if (col 2, 2->1
	        }
	  
	        return completedBoxes;
	    }
	  
	    // 评估函数 - 计算当前局面得分
	    int evaluate() const {
	        // 简单评估：当前玩家分数 - 对手分数
	        if (currentPlayer == 1) {
	            return player1Score - player2Score;
	        } else {
	            return player2Score - player1Score;
	        }
	    }
	  
	    // 打印棋盘
	    void printBoard() const {
	        for (int i = 0; i > findBestMove(DotsAndBoxes& game) {
	        int bestValue = std::numeric_limits::min();
	        std::pair> bestMove = {-1, {-1, -1} };
	        
	        auto validMoves = game.getValidMoves();
	        
	        for (const auto& move : validMoves) {
	            DotsAndBoxes newGame = game;
	            int completed = newGame.makeMove(move.first, move.second.first, move.second.second);
	            
	            int moveValue;
	            if (completed > 0) {
	                // 如果完成了格子，继续当前玩家的回合
	                moveValue = miniMax(newGame, maxDepth, true, 
	                                  std::numeric_limits::min(), 
	                                  std::numeric_limits::max());
	            } else {
	                // 如果没有完成格子，切换玩家
	                moveValue = miniMax(newGame, maxDepth - 1, false, 
	                                  std::numeric_limits::min(), 
	                                  std::numeric_limits::max());
	            }
	            
	            if (moveValue > bestValue) {
	                bestValue = moveValue;
	                bestMove = move;
	            }
	        }
	        
	        return bestMove;
	    }
	  
	  private:
	    // MiniMax算法 with Alpha-Beta剪枝
	    int miniMax(DotsAndBoxes& game, int depth, bool isMaximizingPlayer, 
	                int alpha, int beta) {
	        // 终止条件
	        if (depth == 0 || game.isGameOver()) {
	            return game.evaluate();
	        }
	        
	        auto validMoves = game.getValidMoves();
	        
	        if (isMaximizingPlayer) {
	            int bestValue = std::numeric_limits::min();
	            
	            for (const auto& move : validMoves) {
	                DotsAndBoxes newGame = game;
	                int completed = newGame.makeMove(move.first, move.second.first, move.second.second);
	                
	                int value;
	                if (completed > 0) {
	                    // 继续当前玩家的回合
	                    value = miniMax(newGame, depth, true, alpha, beta);
	                } else {
	                    // 切换玩家
	                    value = miniMax(newGame, depth - 1, false, alpha, beta);
	                }
	                
	                bestValue = std::max(bestValue, value);
	                alpha = std::max(alpha, bestValue);
	                
	                if (beta ::max();
	            
	            for (const auto& move : validMoves) {
	                DotsAndBoxes newGame = game;
	                int completed = newGame.makeMove(move.first, move.second.first, move.second.second);
	                
	                int value;
	                if (completed > 0) {
	                    // 继续当前玩家的回合
	                    value = miniMax(newGame, depth, false, alpha, beta);
	                } else {
	                    // 切换玩家
	                    value = miniMax(newGame, depth - 1, true, alpha, beta);
	                }
	                
	                bestValue = std::min(bestValue, value);
	                beta = std::min(beta, bestValue);
	                
	                if (beta > choice;
	            
	            if (choice  validMoves.size()) {
	                std::cout  0) {
	                std::cout  0) {
	                std::cout  0) {
	    // 继续当前玩家的回合
	    value = miniMax(newGame, depth, true, alpha, beta);
	  } else {
	    // 切换玩家
	    value = miniMax(newGame, depth - 1, false, alpha, beta);
	  }
	  ```
	  
	  当玩家完成格子时，保持当前玩家不变，继续搜索。
- ### 4. 性能优化
	  
	  1. **深度限制**：设置最大搜索深度防止无限递归
	  2. **局面复制**：每次递归创建新的游戏状态
	  3. **移动排序**：可以进一步优化，优先搜索可能的好着法
- ### 5. 使用示例
	  
	  程序提供完整的人机对战界面：
- 人类玩家选择数字进行移动
- AI自动计算最佳着法
- 实时显示棋盘状态和分数
	  
	  这个实现完整展示了点格棋的规则处理和博弈算法，可以根据需要调整棋盘大小和AI搜索深度来平衡性能和棋力。
- 10.12凌晨搞出来的

```C++
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  using namespace std;
	  
	  const int N = 3; // N x N 个格子，棋盘大小为 (2*N+1) x (2*N+1)
	  
	  class GameState {
	  private:
	      int xsize, ysize;
	      vector> board;
	      int curr_player; // 0: 玩家A, 1: 玩家B
	      vector scores;
	      
	      // 棋盘元素类型
	      const int GRID_EDGE = 4;        // 未被标记的边
	      const int GRID_EDGE_USED = 6;   // 被标记的边
	      const int GRID_BOX = 1;         // 未占用的格子
	      const int GRID_BOX_A = 3;       // 玩家A占用的格子
	      const int GRID_BOX_B = 7;       // 玩家B占用的格子
	      const int GRID_DOT = 2;         // 格点
	      
	      vector> dirs = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
	      vector>>> stlist; // 历史状态
	  
	  public:
	      GameState() : xsize(2*N+1), ysize(2*N+1), curr_player(0), scores({0, 0}) {
	          // 初始化棋盘
	          board.resize(ysize, vector(xsize, 0)); // board[行][列]
	          for (int y = 0; y = 0 && x = 0 && y > legal_actions() {
	          vector> actions;
	          for (int y = 0; y  action) {
	          int x = action.first, y = action.second;
	          vector num_lines(2, 0);
	          int idx_lines = 0;
	          
	          for (int i = 0; i  give_best_response() {
	          auto actions = legal_actions();
	          if (actions.empty()) return {-1, -1};
	          
	          vector evals;
	          for (const auto& action : actions) {
	              evals.push_back(eval_action(action));
	          }
	          
	          auto max_it = max_element(evals.begin(), evals.end());
	          int best_idx = distance(evals.begin(), max_it);
	          return actions[best_idx];
	      }
	  
	      // 本地游戏模式
	      void play_local_game() {
	          int board_size = get_board_size();
	          int total_boxes = get_total_boxes();
	          int max_coord = get_xsize() - 1;
	          
	          cout > x >> y;
	                  
	                  if (!is_valid_move(x, y)) {
	                      cout  scores[1]) {
	              cout  scores[0]) {
	              cout 
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  using namespace std;
	  
	  // 程序员可以在这里修改棋盘大小和AI搜索深度
	  const int N = 3; // N x N 个格子，棋盘大小为 (2*N+1) x (2*N+1)
	  const int AI_SEARCH_DEPTH = 7; // MiniMax算法的搜索深度
	  
	  class GameState {
	  private:
	      int xsize, ysize;
	      vector> board;
	      int curr_player; // 0: 玩家A, 1: 玩家B
	      vector scores;
	      
	      // 棋盘元素类型
	      const int GRID_EDGE = 4;        // 未被标记的边
	      const int GRID_EDGE_USED = 6;   // 被标记的边
	      const int GRID_BOX = 1;         // 未占用的格子
	      const int GRID_BOX_A = 3;       // 玩家A占用的格子
	      const int GRID_BOX_B = 7;       // 玩家B占用的格子
	      const int GRID_DOT = 2;         // 格点
	      
	      vector> dirs = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
	      vector>>> stlist; // 历史状态
	  
	  public:
	      GameState() : xsize(2*N+1), ysize(2*N+1), curr_player(0), scores({0, 0}) {
	          // 初始化棋盘
	          board.resize(ysize, vector(xsize, 0)); // board[行][列]
	          for (int y = 0; y = 0 && x = 0 && y > legal_actions() {
	          vector> actions;
	          for (int y = 0; y ::min();
	              
	              for (const auto& move : validMoves) {
	                  // 执行移动
	                  bool scored = do_action(move.first, move.second);
	                  
	                  int value;
	                  if (scored) {
	                      // 如果得分了，继续当前玩家的回合
	                      value = miniMax(depth, true, alpha, beta);
	                  } else {
	                      // 如果没有得分，切换玩家
	                      value = miniMax(depth - 1, false, alpha, beta);
	                  }
	                  
	                  // 撤销移动
	                  undo_action();
	                  
	                  bestValue = max(bestValue, value);
	                  alpha = max(alpha, bestValue);
	                  
	                  if (beta ::max();
	              
	              for (const auto& move : validMoves) {
	                  // 执行移动
	                  bool scored = do_action(move.first, move.second);
	                  
	                  int value;
	                  if (scored) {
	                      // 如果得分了，继续当前玩家的回合
	                      value = miniMax(depth, false, alpha, beta);
	                  } else {
	                      // 如果没有得分，切换玩家
	                      value = miniMax(depth - 1, true, alpha, beta);
	                  }
	                  
	                  // 撤销移动
	                  undo_action();
	                  
	                  bestValue = min(bestValue, value);
	                  beta = min(beta, bestValue);
	                  
	                  if (beta  give_best_response() {
	          auto actions = legal_actions();
	          if (actions.empty()) return {-1, -1};
	          
	          int bestValue = numeric_limits::min();
	          pair bestMove = {-1, -1};
	          
	          for (const auto& move : actions) {
	              // 执行移动
	              bool scored = do_action(move.first, move.second);
	              
	              int moveValue;
	              if (scored) {
	                  // 如果得分了，继续当前玩家的回合
	                  moveValue = miniMax(AI_SEARCH_DEPTH, true, 
	                                    numeric_limits::min(), 
	                                    numeric_limits::max());
	              } else {
	                  // 如果没有得分，切换玩家
	                  moveValue = miniMax(AI_SEARCH_DEPTH - 1, false, 
	                                    numeric_limits::min(), 
	                                    numeric_limits::max());
	              }
	              
	              // 撤销移动
	              undo_action();
	              
	              if (moveValue > bestValue) {
	                  bestValue = moveValue;
	                  bestMove = move;
	              }
	          }
	          
	          return bestMove;
	      }
	  
	      // 本地游戏模式
	      void play_local_game() {
	          int board_size = get_board_size();
	          int total_boxes = get_total_boxes();
	          int max_coord = get_xsize() - 1;
	          
	          cout > x >> y;
	  	            
	  	            if (!is_valid_move(x, y)) {
	  	                cout  scores[1]) {
	              cout  scores[0]) {
	              cout  action) {
	    int x = action.first, y = action.second;
	    vector num_lines(2, 0);  // 存储相邻两个格子的已完成边数
	    int idx_lines = 0;
	    
	    // 检查该边会影响到的格子（最多2个）
	    for (int i = 0; i  give_best_response(const GameState& state) {
	    auto actions = legal_actions(state);  // 获取所有合法移动
	    if (actions.empty()) return {-1, -1};
	    
	    vector evals;
	    // 为每个移动评分
	    for (const auto& action : actions) {
	        evals.push_back(eval_action(state, action));
	    }
	    
	    // 选择评分最高的移动
	    auto max_it = max_element(evals.begin(), evals.end());
	    int best_idx = distance(evals.begin(), max_it);
	    return actions[best_idx];
	  }
	  ```
- ## 五、游戏流程控制
- ### 5.1 主游戏循环
	  ```cpp
	  void play_local_game() {
	    GameState state;
	    init_game_state(state);
	    
	    while (!finished(state)) {
	        display_board(state);
	        
	        if (state.curr_player == 0) {
	            // 人类玩家回合
	            // 输入验证和执行
	        } else {
	            // AI玩家回合
	            auto best_move = give_best_response(state);
	            bool scored = do_action(state, best_move.first, best_move.second);
	            
	            if (!scored) {
	                change_turn(state);  // 只有没得分时才切换玩家
	            }
	        }
	    }
	  }
	  ```
- ### 5.2 回合机制
- 玩家画一条边
- 如果完成任何格子：
  - 玩家得分
  - **继续当前玩家的回合**
- 如果没完成格子：
  - 切换到对方玩家
- ## 六、AI算法特点分析
- ### 6.1 优点
	  1. **简单高效**：只评估当前局面，计算量小
	  2. **策略合理**：优先考虑直接得分和避免给对手机会
	  3. **实时响应**：即使在较大棋盘上也能快速决策
- ### 6.2 局限性
	  1. **缺乏前瞻性**：只考虑当前移动，不模拟后续步骤
	  2. **固定策略**：评估函数权重固定，容易被针对性破解
	  3. **不考虑全局**：可能错过需要多步准备的复杂策略
- ### 6.3 改进方向
	  1. 实现MiniMax算法或Alpha-Beta剪枝进行多步前瞻
	  2. 添加开局库和终局数据库
	  3. 使用机器学习动态调整评估权重
	  
	  这个AI实现了一个**基于规则的贪心算法**，在大多数情况下能够做出合理的决策，特别适合初学者理解点格棋的基本策略。
- 10.15tmp- 我来分析一下这个点格棋博弈中MiniMax算法的实现，并按照要求修改代码。
- ## 原代码MiniMax算法分析
- ### 优点：
	  1. **正确处理连续回合**：当玩家得分时，保持当前玩家继续行动
	  2. **Alpha-Beta剪枝**：已正确实现剪枝逻辑
	  3. **状态保存与恢复**：使用历史栈来撤销动作
- ### 问题：
	  1. **深度控制不一致**：得分时不减少深度可能导致搜索过深
	  2. **评估函数简单**：只考虑当前分数差，没有考虑潜在威胁
	  3. **效率问题**：没有对动作进行排序优化剪枝效果
- ## 改进后的代码
	  
	  ```cpp
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  using namespace std;
	  
	  // 程序员可以在这里修改棋盘大小和AI搜索深度
	  const int N = 3; // N x N 个格子，棋盘大小为 (2*N+1) x (2*N+1)
	  const int AI_SEARCH_DEPTH = 7; // MiniMax算法的搜索深度
	  
	  class GameState {
	  private:
	    int xsize, ysize;
	    vector> board;
	    int curr_player; // 0: 玩家A, 1: 玩家B
	    vector scores;
	    
	    // 棋盘元素类型
	    const int GRID_EDGE = 4;        // 未被标记的边
	    const int GRID_EDGE_USED = 6;   // 被标记的边
	    const int GRID_BOX = 1;         // 未占用的格子
	    const int GRID_BOX_A = 3;       // 玩家A占用的格子
	    const int GRID_BOX_B = 7;       // 玩家B占用的格子
	    const int GRID_DOT = 2;         // 格点
	    
	    vector> dirs = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
	    vector>>> stlist; // 历史状态
	  
	  public:
	    GameState() : xsize(2*N+1), ysize(2*N+1), curr_player(0), scores({0, 0}) {
	        // 初始化棋盘
	        board.resize(ysize, vector(xsize, 0)); // board[行][列]
	        for (int y = 0; y = 0 && x = 0 && y > legal_actions() {
	        vector> actions;
	        for (int y = 0; y > get_sorted_actions() {
	        auto actions = legal_actions();
	        
	        // 为每个动作评分
	        vector> scored_actions; // (分数, x, y)
	        
	        for (const auto& action : actions) {
	            int x = action.first, y = action.second;
	            int score = 0;
	            
	            // 检查这个动作是否会完成格子
	            for (int i = 0; i (a) > get(b); });
	        
	        vector> sorted_actions;
	        for (const auto& item : scored_actions) {
	            sorted_actions.push_back({get(item), get(item)});
	        }
	        
	        return sorted_actions;
	    }
	  
	    // 改进的MiniMax算法 with Alpha-Beta剪枝
	    int miniMax(int depth, bool isMaximizingPlayer, int alpha, int beta) {
	        // 终止条件
	        if (depth == 0 || finished()) {
	            return evaluate();
	        }
	        
	        auto validMoves = get_sorted_actions(); // 使用排序后的动作
	        
	        if (isMaximizingPlayer) {
	            int bestValue = numeric_limits::min();
	            
	            for (const auto& move : validMoves) {
	                // 执行移动
	                bool scored = do_action(move.first, move.second);
	                
	                int value;
	                if (scored) {
	                    // 如果得分了，继续当前玩家的回合，但深度减1
	                    value = miniMax(depth - 1, true, alpha, beta);
	                } else {
	                    // 如果没有得分，切换玩家，深度减1
	                    value = miniMax(depth - 1, false, alpha, beta);
	                }
	                
	                // 撤销移动
	                undo_action();
	                
	                bestValue = max(bestValue, value);
	                alpha = max(alpha, bestValue);
	                
	                if (beta ::max();
	            
	            for (const auto& move : validMoves) {
	                // 执行移动
	                bool scored = do_action(move.first, move.second);
	                
	                int value;
	                if (scored) {
	                    // 如果得分了，继续当前玩家的回合，但深度减1
	                    value = miniMax(depth - 1, false, alpha, beta);
	                } else {
	                    // 如果没有得分，切换玩家，深度减1
	                    value = miniMax(depth - 1, true, alpha, beta);
	                }
	                
	                // 撤销移动
	                undo_action();
	                
	                bestValue = min(bestValue, value);
	                beta = min(beta, bestValue);
	                
	                if (beta  give_best_response() {
	        auto actions = get_sorted_actions(); // 使用排序后的动作
	        if (actions.empty()) return {-1, -1};
	        
	        int bestValue = numeric_limits::min();
	        pair bestMove = actions[0]; // 默认选择第一个动作
	        
	        for (const auto& move : actions) {
	            // 执行移动
	            bool scored = do_action(move.first, move.second);
	            
	            int moveValue;
	            if (scored) {
	                // 如果得分了，继续当前玩家的回合
	                moveValue = miniMax(AI_SEARCH_DEPTH - 1, true, 
	                                  numeric_limits::min(), 
	                                  numeric_limits::max());
	            } else {
	                // 如果没有得分，切换玩家
	                moveValue = miniMax(AI_SEARCH_DEPTH - 1, false, 
	                                  numeric_limits::min(), 
	                                  numeric_limits::max());
	            }
	            
	            // 撤销移动
	            undo_action();
	            
	            if (moveValue > bestValue) {
	                bestValue = moveValue;
	                bestMove = move;
	            }
	        }
	        
	        return bestMove;
	    }
	  
	    // 本地游戏模式
	    void play_local_game() {
	        int board_size = get_board_size();
	        int total_boxes = get_total_boxes();
	        int max_coord = get_xsize() - 1;
	        
	        cout > x >> y;
	             
	             if (!is_valid_move(x, y)) {
	                 cout  scores[1]) {
	            cout  scores[0]) {
	            cout 
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  #include
	  using namespace std;
	  
	  // 程序员可以在这里修改棋盘大小和AI搜索深度
	  const int N = 3; // N x N 个格子，棋盘大小为 (2*N+1) x (2*N+1)
	  const int AI_SEARCH_DEPTH = 7; // MiniMax算法的搜索深度
	  
	  class GameState {
	  private:
	    int xsize, ysize;
	    vector> board;
	    int curr_player; // 0: 玩家A, 1: 玩家B
	    vector scores;
	    
	    // 棋盘元素类型
	    const int GRID_EDGE = 4;        // 未被标记的边
	    const int GRID_EDGE_USED = 6;   // 被标记的边
	    const int GRID_BOX = 1;         // 未占用的格子
	    const int GRID_BOX_A = 3;       // 玩家A占用的格子
	    const int GRID_BOX_B = 7;       // 玩家B占用的格子
	    const int GRID_DOT = 2;         // 格点
	    
	    vector> dirs = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
	    vector>>> stlist; // 历史状态
	  
	  public:
	    GameState() : xsize(2*N+1), ysize(2*N+1), curr_player(0), scores({0, 0}) {
	        // 初始化棋盘
	        board.resize(ysize, vector(xsize, 0)); // board[行][列]
	        for (int y = 0; y = 0 && x = 0 && y > legal_actions() {
	        vector> actions;
	        for (int y = 0; y > get_sorted_actions() {
	        auto actions = legal_actions();
	        
	        // 为每个动作评分并排序
	        vector> scored_actions;
	        for (const auto& action : actions) {
	            int action_score = evaluate_action(action.first, action.second);
	            scored_actions.push_back({action_score, action.first, action.second});
	        }
	        
	        // 按评分降序排序（高价值动作优先）
	        sort(scored_actions.begin(), scored_actions.end(), 
	             [](const auto& a, const auto& b) { return get(a) > get(b); });
	        
	        vector> sorted_actions;
	        for (const auto& item : scored_actions) {
	            sorted_actions.push_back({get(item), get(item)});
	        }
	        
	        return sorted_actions;
	    }
	  
	    // 改进的MiniMax算法 with Alpha-Beta剪枝
	    int miniMax(int depth, bool isMaximizingPlayer, int alpha, int beta) {
	        // 终止条件：达到深度限制或游戏结束
	        if (depth == 0 || finished()) {
	            return evaluate();
	        }
	        
	        // 使用排序后的动作提高剪枝效率
	        auto validMoves = get_sorted_actions();
	        
	        if (isMaximizingPlayer) {
	            int maxEval = numeric_limits::min();
	            
	            for (const auto& move : validMoves) {
	                // 执行移动
	                bool scored = do_action(move.first, move.second);
	                
	                int eval;
	                if (scored) {
	                    // 如果得分了，继续当前玩家的回合（深度不变）
	                    eval = miniMax(depth, true, alpha, beta);
	                } else {
	                    // 如果没有得分，切换玩家（深度减1）
	                    eval = miniMax(depth - 1, false, alpha, beta);
	                }
	                
	                // 撤销移动
	                undo_action();
	                
	                maxEval = max(maxEval, eval);
	                alpha = max(alpha, eval);
	                
	                // Alpha-Beta剪枝
	                if (beta ::max();
	            
	            for (const auto& move : validMoves) {
	                // 执行移动
	                bool scored = do_action(move.first, move.second);
	                
	                int eval;
	                if (scored) {
	                    // 如果得分了，继续当前玩家的回合（深度不变）
	                    eval = miniMax(depth, false, alpha, beta);
	                } else {
	                    // 如果没有得分，切换玩家（深度减1）
	                    eval = miniMax(depth - 1, true, alpha, beta);
	                }
	                
	                // 撤销移动
	                undo_action();
	                
	                minEval = min(minEval, eval);
	                beta = min(beta, eval);
	                
	                // Alpha-Beta剪枝
	                if (beta  give_best_response() {
	        auto actions = get_sorted_actions();
	        if (actions.empty()) return {-1, -1};
	        
	        int bestValue = numeric_limits::min();
	        pair bestMove = actions[0]; // 默认选择第一个（评分最高的）动作
	        
	        // 初始化Alpha-Beta值
	        int alpha = numeric_limits::min();
	        int beta = numeric_limits::max();
	        
	        for (const auto& move : actions) {
	            // 执行移动
	            bool scored = do_action(move.first, move.second);
	            
	            int moveValue;
	            if (scored) {
	                // 如果得分了，继续当前玩家的回合
	                moveValue = miniMax(AI_SEARCH_DEPTH, true, alpha, beta);
	            } else {
	                // 如果没有得分，切换玩家
	                moveValue = miniMax(AI_SEARCH_DEPTH - 1, false, alpha, beta);
	            }
	            
	            // 撤销移动
	            undo_action();
	            
	            // 更新最佳移动
	            if (moveValue > bestValue) {
	                bestValue = moveValue;
	                bestMove = move;
	            }
	            
	            // 更新alpha值
	            alpha = max(alpha, bestValue);
	        }
	        
	        return bestMove;
	    }
	  
	    // 本地游戏模式
	    void play_local_game() {
	        int board_size = get_board_size();
	        int total_boxes = get_total_boxes();
	        int max_coord = get_xsize() - 1;
	        
	        cout > x >> y;
	             
	             if (!is_valid_move(x, y)) {
	                 cout  scores[1]) {
	            cout  scores[0]) {
	            cout ::min();
		    for(auto& move : validMoves){
		        bool scored = do_action(move.first, move.second);
		        int eval;
		        if(scored){
		            eval = miniMax(depth, true, alpha, beta);  // 继续当前玩家
		        } else {
		            eval = miniMax(depth-1, false, alpha, beta); // 切换玩家
		        }
		        undo_action();
		        maxEval = max(maxEval, eval);
		        alpha = max(alpha, eval);
		        if(beta ::max();
		    for(auto& move : validMoves){
		        bool scored = do_action(move.first, move.second);
		        int eval;
		        if(scored) eval = miniMax(depth, false, alpha, beta);
		        else eval = miniMax(depth-1, true, alpha, beta);
		        undo_action();
		        minEval = min(minEval, eval);
		        beta = min(beta, eval);
		        if(beta > get_sorted_actions()
		  ```
  - **启发式排序**：使用`evaluate_action()`对动作预评分
  - **剪枝效率**：高价值动作优先搜索，提高Alpha-Beta剪枝效果
  - ### 3. **状态管理**
		  ```cpp
		  bool scored = do_action(move.first, move.second);
		  // ... 递归搜索 ...
		  undo_action();
		  ```
  - **动作模拟**：执行动作进入新状态
  - **状态恢复**：递归返回后撤销动作，保持状态一致性
  - ## 算法优势
		  
		  1. **深度控制灵活**：正确处理连续得分情况
		  2. **评估全面**：综合考虑当前分数和潜在威胁
		  3. **剪枝高效**：结合动作排序的Alpha-Beta剪枝
		  4. **状态安全**：完善的状态保存和恢复机制
  - ## 潜在改进点
		  
		  1. **评估函数细化**：可以考虑链式反应和长期策略
		  2. **深度动态调整**：根据局面复杂度调整搜索深度
		  3. **开局库**：添加常见开局模式
		  4. **终局优化**：终局阶段使用更精确的搜索策略
- 备注
  - 可以宏定义棋盘大小和搜索深度
  - 改成了struct（懒得用class管理权限）
  - 棋盘输入的坐标（x,y）是放在第四象限的直角坐标系输入
		-
- 待优化
  - 完全基于搜索，导致前几步在给定深度下的搜索开销很大，导致AI思考时间很长
		  -> 考虑优化前几步的思考逻辑
  - 评估函数简单
		  ->可以考虑链式反应和长期策略
  - TODO 考虑根据时间动态调整深度（比如在简单局面实现穷举来实现大幅度提升胜率）
  - 大致思路，根据剩余
  - 每次局面重新存储一个棋盘，复制导致时间开销
- Code

```C++
		  #include
		  #include
		  #include
		  #include
		  #include
		  #include
		  #include
		  #include
		  #include
		  using namespace std;
		  #define endl '\n'
		  
		  // 程序员可以在这里修改棋盘大小和AI搜索深度 int N=3;// N x N 个格子，棋盘大小为(2*N+1)x(2*N+1)int AI_SEARCH_DEPTH=7;// MiniMax算法的搜索深度
		  const int N=3,AI_SEARCH_DEPTH=7;
		  // 棋盘元素类型
		  const int GRID_EDGE=4;       // 未被标记的边
		  const int GRID_EDGE_USED=6;  // 被标记的边
		  const int GRID_BOX=1;        // 未占用的格子
		  const int GRID_BOX_A=3;      // 玩家A占用的格子
		  const int GRID_BOX_B=7;      // 玩家B占用的格子
		  const int GRID_DOT=2;        // 格点
		  int dir[4][2]={ {-1,0},{1,0},{0,-1},{0,1} };
		  
		  struct GameState {
		      int xsize,ysize;
		      vector> board;
		      int curr_player;// 0: 玩家A,1: 玩家B
		      vector scores;
		      vector>>> stlist;// 历史状态
		  
		      GameState(): xsize(2*N+1),ysize(2*N+1),curr_player(0),scores({0,0}){
		          // 初始化棋盘
		          board.resize(ysize,vector(xsize,0));// board[行][列]
		          for(int y=0;y=0&&x=0&&y(state);
		          scores[0]=get(state);
		          scores[1]=get(state);
		          board=get(state);
		          return true;
		      }
		  
		      vector> legal_actions(){
		          vector> actions;
		          for(int y=0;y> get_sorted_actions(){
		          auto actions=legal_actions();
		          
		          // 为每个动作评分并排序
		          vector> scored_actions;
		          for(auto& action : actions){
		              int action_score=evaluate_action(action.first,action.second);
		              scored_actions.push_back(make_tuple(action_score,action.first,action.second));}
		  	
		          
		          // 按评分降序排序（高价值动作优先）
		          sort(scored_actions.begin(),scored_actions.end(),
		               [](auto& a,auto& b){ return get(a)> get(b);});
		          
		          vector> sorted_actions;
		          for(auto& item : scored_actions){
		              sorted_actions.push_back({get(item),get(item)});}
		  	
		          
		          return sorted_actions;
		      }
		  
		      // 改进的MiniMax算法 with Alpha-Beta剪枝
		      int miniMax(int depth,bool isMaximizingPlayer,int alpha,int beta){
		          // 终止条件：达到深度限制或游戏结束
		          if(depth==0 || finished()){
		              return evaluate();}
		  	
		          
		          // 使用排序后的动作提高剪枝效率
		          auto validMoves=get_sorted_actions();
		          
		          if(isMaximizingPlayer){
		              int maxEval=numeric_limits::min();
		              
		              for(auto& move : validMoves){
		                  // 执行移动
		                  bool scored=do_action(move.first,move.second);
		                  
		                  int eval;
		                  if(scored){
		                      // 如果得分了，继续当前玩家的回合（深度不变）
		                      eval=miniMax(depth,true,alpha,beta);
		                  } else {
		                      // 如果没有得分，切换玩家（深度减1）
		                      eval=miniMax(depth-1,false,alpha,beta);
		                  }
		                  
		                  // 撤销移动
		                  undo_action();
		                  
		                  maxEval=max(maxEval,eval);
		                  alpha=max(alpha,eval);
		                  
		                  // Alpha-Beta剪枝
		                  if(beta::max();
		              
		              for(auto& move : validMoves){
		                  // 执行移动
		                  bool scored=do_action(move.first,move.second);
		  
		                  int eval;
		                  if(scored) eval=miniMax(depth,false,alpha,beta);// 如果得分了，继续当前玩家的回合（深度不变）
		                  else eval=miniMax(depth-1,true,alpha,beta);// 如果没有得分，切换玩家（深度减1）
		                  undo_action(); // 撤销移动
		                  minEval=min(minEval,eval);
		                  beta=min(beta,eval);
		                  // Alpha-Beta剪枝
		                  if(beta give_best_response(){
		          auto actions=get_sorted_actions();
		          if(actions.empty())return {-1,-1};
		          
		          int bestValue=numeric_limits::min();
		          pair bestMove=actions[0];// 默认选择第一个（评分最高的）动作
		          
		          // 初始化Alpha-Beta值
		          int alpha=numeric_limits::min();
		          int beta=numeric_limits::max();
		          
		          for(auto& move : actions){
		              // 执行移动
		              bool scored=do_action(move.first,move.second);
		              
		              int moveValue;
		              if(scored){
		                  // 如果得分了，继续当前玩家的回合
		                  moveValue=miniMax(AI_SEARCH_DEPTH,true,alpha,beta);
		              } else {
		                  // 如果没有得分，切换玩家
		                  moveValue=miniMax(AI_SEARCH_DEPTH-1,false,alpha,beta);
		              }
		              
		              // 撤销移动
		              undo_action();
		              
		              // 更新最佳移动
		              if(moveValue > bestValue){
		                  bestValue=moveValue;
		                  bestMove=move;
		              }
		              
		              // 更新alpha值
		              alpha=max(alpha,bestValue);}
		  	
		          
		          return bestMove;
		      }
		  
		      // 本地游戏模式
		      void play_local_game(){
		          int board_size=N;
		          int total_boxes=N*N;
		          int max_coord=2*N;
		          cout>x>>y;
		                  if(!is_valid_move(x,y)){
		                      cout scores[1]){cout scores[0]){cout
	  using namespace std;
	  #define endl '\n'
	  #define pii pair 
	  #define vi vector
	  #define vvi vector
	  #define pb push_back
	  #define fi first
	  #define se second
	  #define IOS ios::sync_with_stdio(false);cin.tie(0),cout.tie(0);
	  const int N=3,DEPTH=5;
	  // 棋盘元素类型
	  const int GRID_EDGE=4;       // 未被标记的边
	  const int GRID_EDGE_USED=6;  // 被标记的边
	  const int GRID_BOX=1;        // 未占用的格子
	  const int GRID_BOX_A=3;      // 玩家A占用的格子
	  const int GRID_BOX_B=7;      // 玩家B占用的格子
	  const int GRID_DOT=2;        // 格点
	  int dir[4][2]={ {-1,0},{1,0},{0,-1},{0,1} };
	  
	  struct GameState {
	      int xsize,ysize;
	      vvi board;
	      int curr_player;// 0:玩家A,1:玩家B
	      vi scores;
	      vector> stlist;// 历史状态
	      GameState():xsize(2*N+1),ysize(2*N+1),curr_player(0),scores({0,0}){
	          // 初始化棋盘
	          board.resize(ysize,vi(xsize,0));// board[行][列]
	          for(int y=0;y=0&&x=0&&y=0&&x=0&&y(state);
	          scores[0]=get(state);
	          scores[1]=get(state);
	          board=get(state);
	          return true;
	      }
	      vector legal_actions(){//获取当前节点
	          vector actions;
	          for(int y=0;y get_sorted_actions(){
	          auto actions=legal_actions();
	          // 为每个动作评分并排序
	          vector> scored_actions;
	          for(auto& action :actions){
	              int action_score=evaluate_action(action.fi,action.se);
	              scored_actions.pb(make_tuple(action_score,action.fi,action.se));}
	          // 按评分降序排序（高价值动作优先）
	          sort(scored_actions.begin(),scored_actions.end(),[](auto& a,auto& b){ return get(a)> get(b);});
	          vector sorted_actions;
	          for(auto& item :scored_actions) sorted_actions.pb({get(item),get(item)});
	          return sorted_actions;
	      }
	      // 改进的MiniMax算法 with Alpha-Beta剪枝
	      int miniMax(int depth,bool isMaximizingPlayer,int alpha,int beta){
	          // 终止条件：达到深度限制或游戏结束
	          if(depth==0 || over()) return evaluate();
	          // 使用排序后的动作提高剪枝效率
	          auto validMoves=get_sorted_actions();
	          if(isMaximizingPlayer){
	              int maxEval=numeric_limits::min();
	              for(auto& move :validMoves){
	                  // 执行移动
	                  bool scored=do_action(move.fi,move.se);
	                  int eval;
	                  if(scored) eval=miniMax(depth,true,alpha,beta);// 如果得分了，继续当前玩家的回合（深度不变）
	                  else eval=miniMax(depth-1,false,alpha,beta);// 如果没有得分，切换玩家（深度减1）
	                  // 撤销移动
	                  undo_action();
	                  maxEval=max(maxEval,eval);
	                  alpha=max(alpha,eval);
	                  if(beta::max();
	              for(auto& move :validMoves){
	                  // 执行移动
	                  bool scored=do_action(move.fi,move.se);
	                  int eval;
	                  if(scored) eval=miniMax(depth,false,alpha,beta);// 如果得分了，继续当前玩家的回合（深度不变）
	                  else eval=miniMax(depth-1,true,alpha,beta);// 如果没有得分，切换玩家（深度减1）
	                  undo_action(); // 撤销移动
	                  minEval=min(minEval,eval);
	                  beta=min(beta,eval);
	                  // Alpha-Beta剪枝
	                  if(beta::min();
	          pii bestMove=actions[0];// 默认选择第一个（评分最高的）动作
	          // 初始化Alpha-Beta
	          int alpha=numeric_limits::min();
	          int beta=numeric_limits::max();
	          for(auto& move:actions){
	              // 执行移动
	              bool scored=do_action(move.fi,move.se);
	              int moveValue;
	              if(scored) moveValue=miniMax(DEPTH,true,alpha,beta);// 如果得分了，继续当前玩家的回合
	              else moveValue=miniMax(DEPTH-1,false,alpha,beta);// 如果没有得分，切换玩家
	              undo_action(); // 撤销移动
	              if(moveValue>bestValue){// 更新最佳移动
	                  bestValue=moveValue;
	                  bestMove=move;
	              }
	  			alpha=max(alpha,bestValue);
	  		}
	          return bestMove;
	      }
	      // 本地游戏模式
	      void play_local_game(){
	          int board_size=N;
	          int total_boxes=N*N;
	          int max_coord=2*N;
	          cout>x>>y;
	                  if(!is_valid_move(x,y)){
	                      cout scores[1]){cout scores[0]){cout
		  using namespace std;
		  #define endl '\n'
		  #define pii pair 
		  #define vi vector
		  #define vvi vector
		  #define pb push_back
		  #define fi first
		  #define se second
		  #define IOS ios::sync_with_stdio(false);
		  const int N=3,DEPTH=5;
		  // 棋盘元素类型
		  const int GRID_EDGE=4;       // 未被标记的边
		  const int GRID_EDGE_USED=6;  // 被标记的边
		  const int GRID_BOX=1;        // 未占用的格子
		  const int GRID_BOX_A=3;      // 玩家A占用的格子
		  const int GRID_BOX_B=7;      // 玩家B占用的格子
		  const int GRID_DOT=2;        // 格点
		  int dir[4][2]={ {-1,0},{1,0},{0,-1},{0,1} };
		  
		  struct GameState {
		      int xsize,ysize;
		      vvi board;
		      int curr_player;// 0:玩家A,1:玩家B
		      vi scores;
		      vector> stlist;// 历史状态
		      
		      GameState():xsize(2*N+1),ysize(2*N+1),curr_player(0),scores({0,0}){
		          // 初始化棋盘
		          board.resize(ysize,vi(xsize,0));// board[行][列]
		          for(int y=0;y=0&&x=0&&y=0&&x=0&&y(state);
		          scores[0]=get(state);
		          scores[1]=get(state);
		          board=get(state);
		          return true;
		      }
		      
		      vector legal_actions(){
		          vector actions;
		          for(int y=0;y get_sorted_actions(){
		          auto actions=legal_actions();
		          // 为每个动作评分并排序
		          vector> scored_actions;
		          for(auto& action :actions){
		              int action_score=evaluate_action(action.fi,action.se);
		              scored_actions.pb(make_tuple(action_score,action.fi,action.se));
		          }
		          // 按评分降序排序（高价值动作优先）
		          sort(scored_actions.begin(),scored_actions.end(),[](auto& a,auto& b){ 
		              return get(a)> get(b);
		          });
		          vector sorted_actions;
		          for(auto& item :scored_actions) 
		              sorted_actions.pb({get(item),get(item)});
		          return sorted_actions;
		      }
		      
		      // 改进的MiniMax算法 with Alpha-Beta剪枝
		      int miniMax(int depth,bool isMaximizingPlayer,int alpha,int beta){
		          // 终止条件：达到深度限制或游戏结束
		          if(depth==0 || over()) return evaluate();
		          
		          // 使用排序后的动作提高剪枝效率
		          auto validMoves=get_sorted_actions();
		          if(isMaximizingPlayer){
		              int maxEval=numeric_limits::min();
		              for(auto& move :validMoves){
		                  // 执行移动
		                  bool scored=do_action(move.fi,move.se);
		                  int eval;
		                  if(scored) eval=miniMax(depth,true,alpha,beta);// 如果得分了，继续当前玩家的回合（深度不变）
		                  else eval=miniMax(depth-1,false,alpha,beta);// 如果没有得分，切换玩家（深度减1）
		                  // 撤销移动
		                  undo_action();
		                  maxEval=max(maxEval,eval);
		                  alpha=max(alpha,eval);
		                  if(beta::max();
		              for(auto& move :validMoves){
		                  // 执行移动
		                  bool scored=do_action(move.fi,move.se);
		                  int eval;
		                  if(scored) eval=miniMax(depth,false,alpha,beta);// 如果得分了，继续当前玩家的回合（深度不变）
		                  else eval=miniMax(depth-1,true,alpha,beta);// 如果没有得分，切换玩家（深度减1）
		                  undo_action(); // 撤销移动
		                  minEval=min(minEval,eval);
		                  beta=min(beta,eval);
		                  // Alpha-Beta剪枝
		                  if(beta::min();
		          pii bestMove=actions[0];// 默认选择第一个（评分最高的）动作
		          // 初始化Alpha-Beta
		          int alpha=numeric_limits::min();
		          int beta=numeric_limits::max();
		          
		          for(auto& move:actions){
		              // 执行移动
		              bool scored=do_action(move.fi,move.se);
		              int moveValue;
		              if(scored) moveValue=miniMax(DEPTH,true,alpha,beta);// 如果得分了，继续当前玩家的回合
		              else moveValue=miniMax(DEPTH-1,false,alpha,beta);// 如果没有得分，切换玩家
		              undo_action(); // 撤销移动
		              
		              if(moveValue>bestValue){// 更新最佳移动
		                  bestValue=moveValue;
		                  bestMove=move;
		              }
		              alpha=max(alpha,bestValue);
		          }
		          return bestMove;
		      }
		      
		      // 本地游戏模式
		      void play_local_game(){
		          int board_size=N;
		          int total_boxes=N*N;
		          int max_coord=2*N;
		          
		          cout>x>>y)){
		                      cin.clear();
		                      cin.ignore(numeric_limits::max(),'\n');
		                      cout scores[1]) cout scores[0]) cout
	  using namespace std;
	  #define endl '\n'
	  #define pii pair 
	  #define vi vector
	  #define vvi vector
	  #define pb push_back
	  #define fi first
	  #define se second
	  #define IOS ios::sync_with_stdio(false);
	  const int N=3,DEPTH=6;
	  
	  // 棋盘元素类型
	  const int GRID_EDGE=4;       // 未被标记的边
	  const int GRID_EDGE_USED=6;  // 被标记的边
	  const int GRID_BOX=1;        // 未占用的格子
	  const int GRID_BOX_A=3;      // 玩家A占用的格子
	  const int GRID_BOX_B=7;      // 玩家B占用的格子
	  const int GRID_DOT=2;        // 格点
	  int dir[4][2]={ {-1,0},{1,0},{0,-1},{0,1} };
	  
	  // 状态信息结构体，只存储变化的部分
	  struct StateInfo {
	      int curr_player;
	      int scoreA, scoreB;
	      int move_x, move_y;
	      vector> changed_cells; // (y,x,old_value)
	  };
	  
	  struct GameState {
	      int xsize,ysize;
	      vvi board;
	      int curr_player;// 0:玩家A,1:玩家B
	      vi scores;
	      vector stlist;// 历史状态（只存储变化）
	      
	      // 预计算缓存
	      vvi box_line_counts; // 存储每个格子的边数
	      
	      GameState():xsize(2*N+1),ysize(2*N+1),curr_player(0),scores({0,0}){
	          // 初始化棋盘
	          board.resize(ysize,vi(xsize,0));
	          box_line_counts.resize(ysize, vi(xsize, 0));
	          for(int y=0;y=0&&x=0&&y=0&&x=0&&y>& changed_cells){
	          bool scored=false;
	          // 检查四个方向的格子
	          for(int i=0;i= 0; i--){
	              auto& cell = state.changed_cells[i];
	              board[get(cell)][get(cell)] = get(cell);
	          }
	          
	          update_box_line_counts(); // 恢复后更新缓存
	          return true;
	      }
	      
	      vector legal_actions(){
	          vector actions;
	          for(int y=0;y 0) {
	              // 能立即得分是最好的情况
	              score += 25 * completes_boxes;
	              
	              // 如果能完成多个盒子，额外奖励
	              if(completes_boxes >= 2) {
	                  score += 20;
	              }
	          } else {
	              // 不能立即得分时，要谨慎评估
	              
	              if(creates_danger > 0) {
	                  if(creates_danger >= 2) {
	                      // 创造多个三边盒子可能形成有利连锁，有一定价值
	                      score += 8 * creates_danger;
	                  } else {
	                      // 单个三边盒子通常很危险
	                      score -= 15 * creates_danger;
	                  }
	              }
	              
	              // 安全发展的动作给予适当奖励
	              score += 4 * creates_safe;
	              
	              // 特别危险的情况：只创造单个三边盒子且没有其他价值
	              if(creates_danger == 1 && creates_safe == 0) {
	                  score -= 30; // 强烈惩罚这种"送分"行为
	              }
	              
	              // 如果创造了危险但同时也创造了安全发展，适当减轻惩罚
	              if(creates_danger > 0 && creates_safe > 0) {
	                  score += 5 * creates_safe;
	              }
	          }
	          
	          return score;
	      }
	      
	      // 获取排序后的动作列表（使用部分排序优化）
	      vector get_sorted_actions(){
	          auto actions=legal_actions();
	          if(actions.size() > scored_actions;
	          scored_actions.reserve(actions.size());
	          
	          for(auto& action :actions){
	              int action_score=evaluate_action_fast(action.fi,action.se);
	              scored_actions.pb({action_score, action});
	          }
	          
	          // 部分排序：只对前几个高分动作进行完整排序
	          int partial_count = min(12, (int)scored_actions.size());
	          partial_sort(scored_actions.begin(), 
	                      scored_actions.begin() + partial_count,
	                      scored_actions.end(),
	                      [](auto& a,auto& b){ return a.first > b.first; });
	          
	          vector sorted_actions;
	          sorted_actions.reserve(actions.size());
	          for(auto& item : scored_actions){
	              sorted_actions.pb(item.second);
	          }
	          return sorted_actions;
	      }
	      
	      // 改进的MiniMax算法 with Alpha-Beta剪枝和节点限制
	      int miniMax(int depth,bool isMaximizingPlayer,int alpha,int beta,int& node_count){
	          node_count++;
	          
	          // 终止条件：达到深度限制或游戏结束
	          if(depth==0 || over()) return evaluate();
	          
	          // 限制搜索节点数，防止搜索过深
	          if(node_count > 30000) return evaluate();
	          
	          auto validMoves=get_sorted_actions();
	          if(isMaximizingPlayer){
	              int maxEval=numeric_limits::min();
	              for(auto& move :validMoves){
	                  // 执行移动
	                  bool scored=do_action(move.fi,move.se);
	                  int eval;
	                  if(scored) eval=miniMax(depth,true,alpha,beta,node_count);
	                  else eval=miniMax(depth-1,false,alpha,beta,node_count);
	                  
	                  // 撤销移动
	                  undo_action();
	                  maxEval=max(maxEval,eval);
	                  alpha=max(alpha,eval);
	                  if(beta::max();
	              for(auto& move :validMoves){
	                  // 执行移动
	                  bool scored=do_action(move.fi,move.se);
	                  int eval;
	                  if(scored) eval=miniMax(depth,false,alpha,beta,node_count);
	                  else eval=miniMax(depth-1,true,alpha,beta,node_count);
	                  
	                  undo_action();
	                  minEval=min(minEval,eval);
	                  beta=min(beta,eval);
	                  if(beta::min();
	          pii bestMove=actions[0];
	          int alpha=numeric_limits::min();
	          int beta=numeric_limits::max();
	          int node_count = 0;
	          
	          for(auto& move:actions){
	              // 执行移动
	              bool scored=do_action(move.fi,move.se);
	              int moveValue;
	              if(scored) moveValue=miniMax(DEPTH,true,alpha,beta,node_count);
	              else moveValue=miniMax(DEPTH-1,false,alpha,beta,node_count);
	              
	              undo_action();
	              
	              if(moveValue>bestValue){
	                  bestValue=moveValue;
	                  bestMove=move;
	              }
	              alpha=max(alpha,bestValue);
	              
	              // 如果找到明显优势的移动，可以提前返回
	              if(bestValue > 80) break;
	          }
	          return bestMove;
	      }
	      
	      // 本地游戏模式
	      void play_local_game(){
	          int board_size=N;
	          int total_boxes=N*N;
	          int max_coord=2*N;
	          cout>x>>y;
	                  if(!is_valid_move(x,y)){
	                      cout scores[1]){cout scores[0]){cout
		  using namespace std;
		  #define endl '\n'
		  const int N=2,M=1;//N列，M行
		  const int tot=N*M;
		  int EDGE=4;       // 未被标记的边
		  int EDGE_USED=6;  // 被标记的边
		  int BOX=1;        // 未占用的格子
		  int BOX_A=3;      // 玩家A占用的格子
		  int BOX_B=7;      // 玩家B占用的格子
		  int DOT=2;        // 格点
		  int dirx[]={-1,1,0,0},diry[]={0,0,-1,1};
		  int FIRST_PLAYER=0;//0:人类先手,1:AI先手 
		  struct Game{
		  	int xsiz,ysiz;
		  	int cur;//0:A,1:B
		  	vector sco;
		  	vector> brd;
		  	vector>>> his;//历史状态(栈)
		  	//{cur,sco[0],sco[1],brd}
		  	void init(){
		  		xsiz=N(xsiz,0));
		  		for(int y=0;y=0&&x=0&&yN*M/2) return 1;//A赢
		          if(sco[1]>N*M/2) return -1;//B赢
		          if(over()){
		              if(sco[0]>sco[1]) return 1;
		              if(sco[1]>sco[0]) return -1;
		              return 0;//平局
		          }return 2;//未结束
		      }
		  
		  	bool update(int x,int y){
		  		bool scored=false;
		  		for(int i=0;i(sta);
		          sco[0]=get(sta);
		          sco[1]=get(sta);
		          brd=get(sta);
		  		//auto [c,s0,s1,b]=his.back();
		  		//his.pop_back();
		  		//cur=c,sco[0]=s0,sco[1]=s1,brd=b;
		  	}
		  	vector> legal_acts(){
		  		vector> acts;
		  		for(int y=0;y response(){
		  		auto acts=legal_acts();
		  		if(acts.empty()) return {-1,-1};
		  		cout bestMove=acts[0];
		  		int tot=0;
		  		//bool isAITurn=true;
		  		for(auto a:acts){
		  			int x=a.first,y=a.second;
		  			int nodes=0;
		  			bool scored=act(x,y);
		  			int moveVal;
		  			if(scored) moveVal=alpha_beta(-2,2,true,nodes);
		  			else{
		  				cur^=1;
		  				moveVal=alpha_beta(-2,2,false,nodes);
		  				cur^=1;
		  			}
		  			undo();
		  			coutbestVal){
		  				bestMove=a;
		  				bestVal=moveVal;
		  			}
		  			tot+=nodes;
		  			if(bestVal==1){
		  				cout>FIRST_PLAYER;
		  	Game state;
		  	state.init();
		  	while(!state.over()){
		  		cout>x>>y)){
		                  cin.clear();
		                  cin.ignore(numeric_limits::max(),'\n');
		                  coutstate.sco[1]) coutstate.sco[0]) cout<<"玩家B获胜!"<<endl;
		      else cout<<"平局！"<<endl;
		  	return 0;
		  }
		  ```
- 忽略错误输入导致的流错误后，貌似已经能做到该赢必赢了（能赢的话ai会输出存在必胜策略）
- 基本上就是第一步可选步数的阶乘的复杂度
- 目前最多能跑2*3
-