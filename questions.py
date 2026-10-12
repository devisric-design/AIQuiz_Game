"""
Question bank for DSC401-6 Artificial Intelligence - Units I & II quiz game.
Each question is a dict with:
  type, topic, level, q, answer, exp (explanation), hint,
  options (choice types) | accept (fill-in-the-blank) | pairs (match),
  real (real-world application?), search (search / state-space problem?)
"""

AR_OPTIONS = [
    "Both A and R are true, and R is the correct explanation of A",
    "Both A and R are true, but R is NOT the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true",
]
TF_OPTIONS = ["True", "False"]

QUESTIONS = []


def add(qtype, topic, level, q, answer, exp, hint, options=None, pairs=None,
        accept=None, real=False, search=False):
    QUESTIONS.append(dict(
        type=qtype, topic=topic, level=level, q=q, answer=answer, exp=exp,
        hint=hint, options=options, pairs=pairs, accept=accept,
        real=real, search=search,
    ))


# ----------------------------------------------------------------------------
# FOUNDATIONS & APPLICATIONS OF AI
# ----------------------------------------------------------------------------
add("MCQ", "Foundations & Applications", "Easy",
    "Which statement best describes Artificial Intelligence?",
    "Building machines that can perform tasks which normally require human intelligence",
    "AI is the science and engineering of making machines perceive, reason, learn and act in ways we associate with human intelligence.",
    "Think perception, reasoning, learning and decision-making.",
    options=["Building machines that can perform tasks which normally require human intelligence",
             "Writing programs that only perform very fast arithmetic",
             "Storing very large amounts of data in databases",
             "Designing faster computer hardware"])

add("MCQ", "Foundations & Applications", "Easy",
    "Russell & Norvig describe four approaches to AI. Which one is NOT among them?",
    "Acting emotionally",
    "The four approaches are: thinking humanly, thinking rationally, acting humanly and acting rationally.",
    "Two approaches are about thought processes, two about behaviour.",
    options=["Thinking humanly", "Thinking rationally", "Acting rationally", "Acting emotionally"])

add("Scenario", "Foundations & Applications", "Medium",
    "A hospital uses software that examines retinal photographs and flags patients likely to have diabetic retinopathy. "
    "Which AI area is mainly being applied?",
    "Computer vision combined with machine learning",
    "Interpreting image content is a computer-vision task, and the diagnostic pattern is learned from labelled images by machine learning.",
    "The input to the system is an image.",
    options=["Computer vision combined with machine learning",
             "Natural language generation",
             "Robotic motion planning",
             "Constraint satisfaction"],
    real=True)

# ----------------------------------------------------------------------------
# TURING TEST
# ----------------------------------------------------------------------------
add("MCQ", "Turing Test", "Easy",
    "A machine passes the Turing Test if...",
    "a human interrogator cannot reliably tell whether the responses come from a machine or a human",
    "In Turing's imitation game, the interrogator converses by text; if they cannot reliably distinguish the machine from a person, the machine passes.",
    "Passing is about being indistinguishable.",
    options=["a human interrogator cannot reliably tell whether the responses come from a machine or a human",
             "it solves a chess position faster than a grandmaster",
             "it can lift physical objects like a human",
             "it stores more facts than any human"])

add("True/False", "Turing Test", "Medium",
    "The basic (text-only) Turing Test requires the machine to have computer vision and a robotic body.",
    "False",
    "Vision and robotics are needed only for the Total Turing Test. The basic test is purely text-based.",
    "Which version of the test adds perception and physical manipulation?",
    options=TF_OPTIONS)

add("MCQ", "Turing Test", "Medium",
    "Which set of capabilities is needed to pass the basic Turing Test?",
    "Natural language processing, knowledge representation, automated reasoning, machine learning",
    "The machine must communicate (NLP), store what it knows (knowledge representation), answer new questions (reasoning) and adapt (learning).",
    "The test is a conversation, so what must a conversing program be able to do?",
    options=["Natural language processing, knowledge representation, automated reasoning, machine learning",
             "Computer vision, robotics, motor control, speech hardware",
             "Database management, networking, compilers, graphics",
             "Sensors, actuators, batteries, wheels"])

add("Scenario", "Turing Test", "Medium",
    "A bank evaluates its text chatbot by letting customers chat without telling them whether a human or the bot is replying. "
    "Which idea does this follow, and what does a 'pass' mean?",
    "Turing Test - customers cannot reliably tell the bot from a human agent",
    "This is an informal version of the imitation game: the bot passes if users cannot reliably distinguish it from a human.",
    "Blind text conversation with a judge is the classic set-up of one famous test.",
    options=["Turing Test - customers cannot reliably tell the bot from a human agent",
             "Hill climbing - the bot reaches a local maximum of accuracy",
             "Turing Test - the bot answers faster than any human agent",
             "Constraint satisfaction - the bot satisfies every customer constraint"],
    real=True)

# ----------------------------------------------------------------------------
# RATIONAL AGENTS
# ----------------------------------------------------------------------------
add("Assertion-Reason", "Rational Agents", "Medium",
    "Assertion (A): A rational agent is not necessarily omniscient.\n\n"
    "Reason (R): Rationality maximises expected performance given the percept sequence to date, not the actual outcome.",
    AR_OPTIONS[0],
    "Rationality is about expected performance given what the agent has perceived. An omniscient agent would know actual outcomes, which is impossible in practice. R correctly explains A.",
    "Expected vs. actual outcome.",
    options=AR_OPTIONS)

add("MCQ", "Rational Agents", "Medium",
    "What a rational agent should do at any moment depends on which four things?",
    "Performance measure, prior knowledge of the environment, available actions, percept sequence",
    "These four factors define rationality: the success criterion, what the agent already knows, what it can do, and what it has perceived so far.",
    "One is the success criterion, one is history of perceptions.",
    options=["Performance measure, prior knowledge of the environment, available actions, percept sequence",
             "CPU speed, memory size, programming language, operating system",
             "Heuristic function, goal test, path cost, branching factor",
             "Sensors, batteries, wheels, cameras"])

# ----------------------------------------------------------------------------
# INTELLIGENT AGENTS
# ----------------------------------------------------------------------------
add("Fill in the Blanks", "Intelligent Agents", "Easy",
    "The mapping from every possible percept sequence to an action is called the agent ________.",
    "function",
    "The agent function is an abstract mathematical description; the agent program is its concrete implementation.",
    "Mathematically, an agent is described by a ______ from percepts to actions.",
    accept=["function", "agent function"])

add("Match the Following", "Intelligent Agents", "Medium",
    "Match each agent type with its description.",
    "See pairs",
    "Simple reflex agents use condition-action rules; model-based agents keep internal state; goal-based agents plan toward goals; utility-based agents trade off conflicting goals using a utility measure.",
    "Ask: does it use memory? goals? a measure of 'how happy' it is?",
    pairs=[("Simple reflex agent", "Acts only on the current percept using condition-action rules"),
           ("Model-based reflex agent", "Maintains an internal state to track unseen parts of the world"),
           ("Goal-based agent", "Chooses actions by searching/planning toward a goal state"),
           ("Utility-based agent", "Maximises a measure of 'happiness' when goals conflict")])

add("MCQ", "Intelligent Agents", "Hard",
    "In a learning agent, which component suggests exploratory actions that lead to new and informative experiences?",
    "Problem generator",
    "The critic gives feedback, the learning element improves the agent, the performance element selects actions, and the problem generator proposes exploratory actions.",
    "Exploration needs something that deliberately suggests new things to try.",
    options=["Critic", "Learning element", "Performance element", "Problem generator"])

# ----------------------------------------------------------------------------
# AGENTS & ENVIRONMENTS
# ----------------------------------------------------------------------------
add("Scenario", "Agents & Environments", "Medium",
    "For a self-driving taxi (PEAS description), which of the following is a SENSOR?",
    "Lidar",
    "Sensors perceive the environment (lidar, cameras, GPS, speedometer). Steering, brakes and horn are actuators.",
    "Sensors perceive, actuators act.",
    options=["Lidar", "Steering control", "Brake actuator", "Horn"],
    real=True)

add("Scenario", "Agents & Environments", "Medium",
    "A robot vacuum cannot see the whole house at once, so it builds a map and remembers which rooms it has already cleaned. "
    "What type of agent is it?",
    "Model-based reflex agent",
    "Because it cannot observe the full state, it keeps an internal model/state of the world and updates it from percepts.",
    "It keeps internal state about parts of the world it cannot currently see.",
    options=["Simple reflex agent", "Model-based reflex agent", "Goal-based agent only", "Table-driven agent"],
    real=True)

add("Scenario", "Agents & Environments", "Hard",
    "A navigation app lets you pick between 'fastest' and 'cheapest' routes and weighs travel time against toll cost to choose the best overall route. "
    "Which agent type does this best describe?",
    "Utility-based agent",
    "Goals alone give only 'achieved / not achieved'. Trading off several conflicting criteria with a numeric preference (utility) is the hallmark of a utility-based agent.",
    "Conflicting objectives are traded off numerically.",
    options=["Simple reflex agent", "Model-based reflex agent", "Goal-based agent", "Utility-based agent"],
    real=True)

add("Scenario", "Agents & Environments", "Easy",
    "A room thermostat switches the heater ON when temperature < 20 C and OFF otherwise. Which agent type is it?",
    "Simple reflex agent",
    "It maps the current percept directly to an action by a condition-action rule, with no memory or planning.",
    "It uses only the current temperature reading.",
    options=["Simple reflex agent", "Model-based reflex agent", "Goal-based agent", "Learning agent"],
    real=True)

# ----------------------------------------------------------------------------
# GOOD BEHAVIOUR
# ----------------------------------------------------------------------------
add("Scenario", "Good Behaviour", "Medium",
    "A vacuum agent is rewarded for each unit of dirt it cleans, so it learns to dump dirt and clean it again. "
    "Which performance measure fixes this?",
    "Reward the agent for each time step in which the floor is clean",
    "Performance measures should reflect the desired state of the environment, not the agent's activity. Rewarding a clean floor removes the incentive to create dirt.",
    "Measure the result you want in the environment, not the effort.",
    options=["Reward the agent for each time step in which the floor is clean",
             "Reward the agent for the total distance it travels",
             "Reward the agent for the amount of dirt collected",
             "Reward the agent for using less battery only"],
    real=True)

add("True/False", "Good Behaviour", "Easy",
    "A performance measure should be designed according to what we actually want in the environment, not according to how we think the agent should behave.",
    "True",
    "This is the standard guideline for specifying good behaviour; otherwise agents can 'game' the measure.",
    "Think of the vacuum-cleaner example.",
    options=TF_OPTIONS)

# ----------------------------------------------------------------------------
# NATURE OF ENVIRONMENTS
# ----------------------------------------------------------------------------
add("True/False", "Nature of Environments", "Easy",
    "In a deterministic environment, the next state is completely determined by the current state and the action executed by the agent.",
    "True",
    "That is the definition of deterministic; otherwise the environment is stochastic (or strategic when other agents' actions create the uncertainty).",
    "No randomness in the transition.",
    options=TF_OPTIONS)

add("Match the Following", "Nature of Environments", "Medium",
    "Match each environment property with its meaning.",
    "See pairs",
    "Episodic: independent episodes; sequential: actions have long-term consequences; dynamic: environment changes while the agent thinks; partially observable: sensors give incomplete information.",
    "Think of image classification (episodic) vs. chess (sequential).",
    pairs=[("Episodic", "Each decision is independent of earlier ones (e.g., image classification)"),
           ("Sequential", "Current action can affect all future decisions (e.g., chess)"),
           ("Dynamic", "Environment can change while the agent is deliberating"),
           ("Partially observable", "Sensors give noisy or incomplete information about the state")])

add("Scenario", "Nature of Environments", "Medium",
    "Which description best fits the task environment of a self-driving car on a busy road?",
    "Partially observable, stochastic, sequential, dynamic, continuous, multi-agent",
    "The car cannot see everything, other drivers behave unpredictably, actions have consequences over time, the world keeps moving, and states/time are continuous.",
    "It is about as hard as an environment gets.",
    options=["Partially observable, stochastic, sequential, dynamic, continuous, multi-agent",
             "Fully observable, deterministic, episodic, static, discrete, single-agent",
             "Fully observable, stochastic, episodic, static, continuous, single-agent",
             "Partially observable, deterministic, episodic, static, discrete, single-agent"],
    real=True)

add("MCQ", "Nature of Environments", "Hard",
    "Chess played with a clock is best classified as:",
    "Fully observable, strategic, sequential, semi-dynamic, discrete, multi-agent",
    "The whole board is visible, the opponent's choice makes outcomes strategic, moves have long-term effects, the clock makes the environment semi-dynamic (the score changes with time though the board does not), and moves are discrete.",
    "The environment itself does not change while you think, but your performance score does.",
    options=["Fully observable, strategic, sequential, semi-dynamic, discrete, multi-agent",
             "Partially observable, stochastic, episodic, dynamic, continuous, single-agent",
             "Fully observable, stochastic, episodic, static, continuous, single-agent",
             "Partially observable, deterministic, episodic, static, discrete, single-agent"])

# ----------------------------------------------------------------------------
# PROBLEMS & PROBLEM SPACES
# ----------------------------------------------------------------------------
add("MCQ", "Problems & Problem Spaces", "Easy",
    "Which of the following is NOT a component of a well-defined search problem?",
    "Learning rate",
    "A well-defined problem has an initial state, actions, a transition model, a goal test and a path cost. Learning rate belongs to machine learning.",
    "Which item belongs to training neural networks?",
    options=["Initial state", "Goal test", "Path cost", "Learning rate"])

add("Fill in the Blanks", "Problems & Problem Spaces", "Medium",
    "The function that checks whether a given state is the desired end state is called the ________ test.",
    "goal",
    "The goal test determines whether a state is a goal state; it can be explicit (a set of states) or implicit (a property such as 'checkmate').",
    "It tells the search when to stop.",
    accept=["goal", "goal state"])

# ----------------------------------------------------------------------------
# STATE SPACE SEARCH
# ----------------------------------------------------------------------------
add("Problem Solving", "State Space Search", "Medium",
    "Water-jug problem: a 4-litre jug and a 3-litre jug, state written as (x, y) = (litres in 4L jug, litres in 3L jug), starting at (0, 0). "
    "Perform: fill the 3L jug -> pour it into the 4L jug -> fill the 3L jug again -> pour from the 3L jug into the 4L jug until the 4L jug is full. "
    "What is the resulting state?",
    "(4, 2)",
    "(0,0) -> (0,3) -> (3,0) -> (3,3) -> pour 1 L to fill the 4L jug -> (4,2).",
    "Trace the state after each operation; the 4L jug can only take 1 more litre at the end.",
    options=["(4, 2)", "(3, 3)", "(4, 3)", "(2, 4)"],
    search=True)

add("Problem Solving", "State Space Search", "Hard",
    "Missionaries and Cannibals (3 missionaries, 3 cannibals, a boat carrying at most 2, cannibals must never outnumber missionaries on a bank where missionaries are present). "
    "What is the minimum number of boat crossings needed to move everyone across?",
    "11",
    "The shortest solution has 11 crossings (6 forward, 5 return trips counted together).",
    "It is an odd number, more than 9.",
    options=["7", "9", "11", "13"],
    search=True)

# ----------------------------------------------------------------------------
# PRODUCTION SYSTEMS
# ----------------------------------------------------------------------------
add("MCQ", "Production Systems", "Easy",
    "The three main components of a production system are:",
    "A global database, a set of production rules, and a control strategy",
    "The database holds the current state, rules (IF condition THEN action) change it, and the control strategy decides which rule to apply next.",
    "Data + rules + something to choose between rules.",
    options=["A global database, a set of production rules, and a control strategy",
             "A compiler, an interpreter, and a debugger",
             "Sensors, actuators, and an environment",
             "A heuristic, a goal test, and a path cost"])

add("MCQ", "Production Systems", "Medium",
    "When several production rules match the current state, which component decides which rule to fire (conflict resolution)?",
    "Control strategy",
    "The control strategy selects among applicable rules and also decides how to handle repeated states.",
    "It is the 'brain' that sequences the rules.",
    options=["Global database", "Production rules", "Control strategy", "Goal test"])

add("Match the Following", "Production Systems", "Hard",
    "Match each problem with its classification in production-system terms.",
    "See pairs",
    "Theorem proving: monotonic and partially commutative. Robot navigation: non-monotonic but partially commutative. Chemical synthesis: monotonic but not partially commutative. Playing bridge: neither.",
    "Monotonic = applying a rule never prevents applying earlier-applicable rules.",
    pairs=[("Theorem proving", "Monotonic, partially commutative"),
           ("Robot navigation", "Non-monotonic, partially commutative"),
           ("Chemical synthesis", "Monotonic, not partially commutative"),
           ("Playing bridge", "Non-monotonic, not partially commutative")])

# ----------------------------------------------------------------------------
# PROBLEM CHARACTERISTICS
# ----------------------------------------------------------------------------
add("MCQ", "Problem Characteristics", "Medium",
    "Chess is an example of which type of problem with respect to solution steps?",
    "Irrecoverable - a move that has been made cannot be undone",
    "In chess, once a move is made it cannot be taken back, so mistakes cannot be recovered by simple backtracking.",
    "Compare with 8-puzzle where you can move a tile back.",
    options=["Irrecoverable - a move that has been made cannot be undone",
             "Ignorable - steps can simply be ignored",
             "Recoverable - any move can be undone by backtracking",
             "Decomposable into independent sub-problems"])

add("MCQ", "Problem Characteristics", "Medium",
    "In the 8-puzzle a wrong move can be undone by moving the tile back. Which category does this make the problem?",
    "Recoverable",
    "Ignorable (theorem proving), recoverable (8-puzzle) and irrecoverable (chess) differ in whether steps can be ignored, undone or neither.",
    "Undoable via backtracking.",
    options=["Ignorable", "Recoverable", "Irrecoverable", "Non-deterministic"])

add("True/False", "Problem Characteristics", "Medium",
    "The Travelling Salesperson Problem is an 'any-path' problem, because any tour that visits all cities is acceptable.",
    "False",
    "TSP is a 'best-path' problem: we need the shortest tour, so all candidate paths must be compared, unlike any-path problems like the water-jug problem.",
    "Is just any tour good enough?",
    options=TF_OPTIONS)

# ----------------------------------------------------------------------------
# ISSUES IN THE DESIGN OF SEARCH PROGRAMS
# ----------------------------------------------------------------------------
add("Fill in the Blanks", "Issues in Search Program Design", "Easy",
    "Searching from the goal state back toward the start state is called ________ search (reasoning).",
    "backward",
    "Forward search (reasoning) starts at the initial state; backward search (reasoning) starts at the goal and works toward the initial state.",
    "Opposite of 'forward'.",
    accept=["backward", "backward search", "backward chaining", "backward reasoning"])

add("MCQ", "Issues in Search Program Design", "Medium",
    "Why does a graph-search algorithm maintain an explored (closed) list?",
    "To avoid re-expanding repeated states and getting trapped in loops",
    "Many paths can lead to the same state; remembering visited states prevents redundant work and infinite loops.",
    "Think 8-puzzle: the same configuration can be reached in many ways.",
    options=["To avoid re-expanding repeated states and getting trapped in loops",
             "To store the heuristic values of every state",
             "To guarantee that the solution is always optimal",
             "To reduce the branching factor to 1"])

add("Scenario", "Issues in Search Program Design", "Hard",
    "From the start state each state has about 30 successors, but the goal state can be reached from only about 2 predecessor states per state. "
    "Which search direction is generally preferable?",
    "Backward search from the goal",
    "Choose the direction with the smaller branching factor. Here backward search branches into 2 rather than 30, so far fewer nodes are generated.",
    "Prefer the direction with fewer branches.",
    options=["Backward search from the goal", "Forward search from the start",
             "Both are always equally good", "Neither can be used"])

# ----------------------------------------------------------------------------
# BREADTH-FIRST SEARCH
# ----------------------------------------------------------------------------
add("MCQ", "Breadth-First Search", "Easy",
    "Breadth-First Search uses which data structure for its frontier?",
    "Queue (FIFO)",
    "BFS expands the shallowest unexpanded node first, which is exactly FIFO order.",
    "First in, first out.",
    options=["Queue (FIFO)", "Stack (LIFO)", "Priority queue by h(n)", "Binary tree"])

add("Problem Solving", "Breadth-First Search", "Medium",
    "A search tree has branching factor b = 3. BFS searches down to depth d = 4. "
    "Including the root, how many nodes are in the tree up to depth 4?",
    "121",
    "1 + 3 + 9 + 27 + 81 = 121. In general (b^(d+1) - 1) / (b - 1), which shows the O(b^d) time/space of BFS.",
    "Add nodes level by level: 1, 3, 9, ...",
    options=["81", "121", "64", "243"],
    search=True)

# ----------------------------------------------------------------------------
# DEPTH-FIRST SEARCH
# ----------------------------------------------------------------------------
add("Fill in the Blanks", "Depth-First Search", "Easy",
    "DFS uses a ________ (LIFO) data structure, which can also be implemented through recursion.",
    "stack",
    "The most recently generated node is expanded first, which is LIFO order.",
    "Last in, first out.",
    accept=["stack", "a stack", "lifo", "lifo stack"])

# Tree used in the next two questions
TREE = ("Consider this tree (children are visited left to right):\n\n"
        "```\n"
        "A -> B, C\n"
        "B -> D, E\n"
        "C -> F\n"
        "E -> G\n"
        "```\n")

add("Problem Solving", "Breadth-First Search", "Medium",
    TREE + "\nIn which order does BFS visit the nodes, starting at A?",
    "A, B, C, D, E, F, G",
    "BFS visits level by level: A | B, C | D, E, F | G.",
    "Level by level.",
    options=["A, B, C, D, E, F, G", "A, B, D, E, G, C, F", "A, C, F, B, D, E, G", "A, B, D, C, F, E, G"],
    search=True)

add("Problem Solving", "Depth-First Search", "Medium",
    TREE + "\nIn which order does DFS visit the nodes, starting at A?",
    "A, B, D, E, G, C, F",
    "DFS goes as deep as possible first: A -> B -> D (dead end) -> back to B -> E -> G -> back to A -> C -> F.",
    "Go deep first, backtrack at dead ends.",
    options=["A, B, D, E, G, C, F", "A, B, C, D, E, F, G", "A, C, F, B, D, E, G", "A, B, D, C, F, E, G"],
    search=True)

# ----------------------------------------------------------------------------
# ITERATIVE DEEPENING
# ----------------------------------------------------------------------------
add("MCQ", "Iterative Deepening", "Medium",
    "Iterative Deepening DFS (IDDFS) is attractive because it combines:",
    "The low memory use of DFS with the completeness and optimality (equal step cost) of BFS",
    "IDDFS repeatedly runs depth-limited DFS with growing limits, needing only O(bd) memory while still finding the shallowest goal.",
    "Best of two worlds.",
    options=["The low memory use of DFS with the completeness and optimality (equal step cost) of BFS",
             "The speed of greedy search with the optimality of A*",
             "The randomness of hill climbing with the memory of BFS",
             "The heuristic guidance of A* with the simplicity of DFS"])

add("Problem Solving", "Iterative Deepening", "Hard",
    "IDDFS is run with depth limits 0, 1, 2 and 3 in turn (goal not found until depth 3). "
    "How many times in total is the root node visited?",
    "4",
    "The root is visited once in every iteration, and there are four iterations (limits 0, 1, 2, 3). Repeated work is small because most nodes lie at the deepest level.",
    "One visit per iteration.",
    options=["1", "3", "4", "8"],
    search=True)

add("Scenario", "Iterative Deepening", "Hard",
    "A chess engine must return a move within 5 seconds, and the depth it can search in that time is unknown. "
    "Which strategy lets it always have a best-so-far move ready when time expires?",
    "Iterative deepening",
    "Searching to depth 1, 2, 3... means a complete result for the previous depth is always available when time runs out. This is how real chess engines manage time.",
    "Finish a shallow search completely before going deeper.",
    options=["Iterative deepening", "Plain DFS to unbounded depth", "Plain BFS", "Random-restart hill climbing"],
    real=True)

# ----------------------------------------------------------------------------
# HILL CLIMBING & VARIATIONS
# ----------------------------------------------------------------------------
add("MCQ", "Hill Climbing", "Easy",
    "Which statement describes hill climbing?",
    "A local search that repeatedly moves to a better neighbouring state without keeping a search tree",
    "Hill climbing only remembers the current state and moves uphill; it does not backtrack or keep alternatives.",
    "It only looks at neighbours of the current state.",
    options=["A local search that repeatedly moves to a better neighbouring state without keeping a search tree",
             "A complete search that expands the shallowest node first",
             "A search that always finds the globally optimal solution",
             "A search that stores every visited state in a queue"])

add("Assertion-Reason", "Hill Climbing", "Medium",
    "Assertion (A): Hill climbing can stop without reaching the global optimum.\n\n"
    "Reason (R): It can get trapped by local maxima, plateaus and ridges.",
    AR_OPTIONS[0],
    "At a local maximum no neighbour is better, so hill climbing halts there. Plateaus (flat areas) and ridges (narrow slopes) also stall it. R explains A.",
    "What happens when no neighbour is better?",
    options=AR_OPTIONS)

add("Match the Following", "Hill Climbing", "Medium",
    "Match each hill-climbing variant with its behaviour.",
    "See pairs",
    "Simple takes the first better neighbour, steepest-ascent evaluates all neighbours, stochastic picks randomly among uphill moves, and random-restart repeats the search from new random starts.",
    "Look at the keywords: first, best, random, restart.",
    pairs=[("Simple hill climbing", "Moves to the first neighbour that is better than the current state"),
           ("Steepest-ascent hill climbing", "Examines all neighbours and moves to the best one"),
           ("Stochastic hill climbing", "Randomly chooses among the uphill moves"),
           ("Random-restart hill climbing", "Repeats the search from random start states to escape local maxima")])

add("Problem Solving", "Hill Climbing", "Medium",
    "The current state has value 5 (higher is better). Its neighbours, examined in order, have values 4, 6 and 8. "
    "Which neighbour is chosen by simple hill climbing and by steepest-ascent hill climbing?",
    "Simple -> 6, Steepest -> 8",
    "Simple hill climbing accepts the first improvement (6). Steepest-ascent compares all neighbours and picks the best (8).",
    "One stops at the first improvement; the other checks everything.",
    options=["Simple -> 6, Steepest -> 8", "Simple -> 8, Steepest -> 6",
             "Simple -> 4, Steepest -> 8", "Both choose 6"],
    search=True)

add("Scenario", "Hill Climbing", "Hard",
    "While tuning a model's hyperparameters, a hill-climbing script keeps ending at a mediocre configuration that depends on its starting values. "
    "Which modification most directly helps?",
    "Random-restart hill climbing",
    "Different random starting points give the search chances to reach different peaks, so the best result across restarts is far more likely to be near the global optimum. Simulated annealing is another remedy.",
    "The result depends on the start point - so change the start point.",
    options=["Random-restart hill climbing", "Always move to the worst neighbour",
             "Use only a single starting point", "Stop after the first step"],
    real=True)

add("True/False", "Hill Climbing", "Medium",
    "Simulated annealing may sometimes accept a move to a worse state, which helps it escape local maxima.",
    "True",
    "Simulated annealing accepts worse moves with a probability that decreases as the 'temperature' cools, allowing escape from local optima.",
    "Unlike pure hill climbing, it does not always go uphill.",
    options=TF_OPTIONS)

# ----------------------------------------------------------------------------
# HEURISTIC SEARCH
# ----------------------------------------------------------------------------
add("MCQ", "Heuristic Search", "Easy",
    "In heuristic search, h(n) represents:",
    "The estimated cost of the cheapest path from node n to a goal",
    "g(n) is the cost so far; h(n) is the estimated remaining cost to the goal.",
    "It is about the future cost, not the past cost.",
    options=["The estimated cost of the cheapest path from node n to a goal",
             "The actual cost from the start to node n",
             "The depth of node n",
             "The number of children of node n"])

add("Problem Solving", "Heuristic Search", "Medium",
    "8-puzzle (blank shown as _):\n\n"
    "```\nCurrent      Goal\n2 8 3        1 2 3\n1 6 4        8 _ 4\n7 _ 5        7 6 5\n```\n"
    "What is the Manhattan-distance heuristic value h(n) of the current state? (Do not count the blank.)",
    "5",
    "Tile 1: 1, tile 2: 1, tile 6: 1, tile 8: 2, others 0. Total = 5 (the misplaced-tiles heuristic would give only 4).",
    "Sum of |row difference| + |column difference| for each tile.",
    options=["3", "4", "5", "6"],
    search=True)

add("Fill in the Blanks", "Heuristic Search", "Medium",
    "In A* search the evaluation function is f(n) = ________ + h(n), where the missing term is the path cost from the start to n.",
    "g(n)",
    "A* combines the cost so far g(n) with the heuristic estimate h(n); it is optimal when h is admissible.",
    "Cost so far.",
    accept=["g(n)", "g", "g (n)"])

add("Scenario", "Heuristic Search", "Medium",
    "A maps application uses A* to find routes between two places. Which heuristic is admissible?",
    "Straight-line (Euclidean) distance to the destination",
    "No road can be shorter than the straight line, so it never over-estimates the true cost, and so is admissible.",
    "An admissible heuristic never over-estimates.",
    options=["Straight-line (Euclidean) distance to the destination",
             "Twice the actual road distance to the destination",
             "The length of the longest highway in the country",
             "Number of traffic signals multiplied by 1000 km"],
    real=True)

# ----------------------------------------------------------------------------
# BEST-FIRST SEARCH
# ----------------------------------------------------------------------------
add("MCQ", "Best-First Search", "Medium",
    "Greedy best-first search selects the next node to expand based on:",
    "f(n) = h(n)",
    "Greedy best-first uses only the heuristic estimate to the goal; A* uses g(n) + h(n); uniform-cost search uses g(n).",
    "It ignores the cost so far.",
    options=["f(n) = h(n)", "f(n) = g(n)", "f(n) = g(n) + h(n)", "f(n) = depth of n"])

add("Problem Solving", "Best-First Search", "Hard",
    "Graph edges and costs: S-A = 1, S-B = 4, A-G = 10, B-G = 3. Heuristic values: h(S) = 3, h(A) = 2, h(B) = 3, h(G) = 0. "
    "What path costs do greedy best-first search and A* return from S to G?",
    "Greedy: 11, A*: 7",
    "Greedy picks A (h = 2) then G, cost 1 + 10 = 11. A* has f(A) = 3 and f(B) = 7; expanding A reaches G with f = 11, but expanding B gives G with f = 7, so A* returns S-B-G with cost 7.",
    "Greedy looks only at h; A* adds the cost so far.",
    options=["Greedy: 11, A*: 7", "Greedy: 7, A*: 11", "Greedy: 11, A*: 11", "Greedy: 7, A*: 7"],
    search=True)

# ----------------------------------------------------------------------------
# MORE ASSERTION-REASON & MATCH (cross-topic)
# ----------------------------------------------------------------------------
add("Assertion-Reason", "Heuristic Search", "Hard",
    "Assertion (A): A* with an inadmissible heuristic is always guaranteed to return an optimal path.\n\n"
    "Reason (R): A* evaluates nodes using f(n) = g(n) + h(n).",
    AR_OPTIONS[3],
    "Optimality of A* requires h to be admissible (and consistent for graph search). R is a true statement but does not guarantee optimality, so A is false.",
    "What property of h is needed for optimality?",
    options=AR_OPTIONS)

add("Assertion-Reason", "Depth-First Search", "Medium",
    "Assertion (A): DFS usually needs much less memory than BFS.\n\n"
    "Reason (R): DFS stores only the current path from the root plus the unexpanded siblings along that path.",
    AR_OPTIONS[0],
    "DFS needs O(b*m) memory, while BFS needs O(b^d). R correctly explains why.",
    "Compare O(bm) with O(b^d).",
    options=AR_OPTIONS)

add("Match the Following", "Breadth-First Search", "Medium",
    "Match each search algorithm with its key property.",
    "See pairs",
    "BFS: FIFO queue; DFS: LIFO stack with linear memory; IDDFS: repeated depth-limited DFS; A*: f(n) = g(n) + h(n).",
    "Think data structure or evaluation function.",
    pairs=[("BFS", "Uses a FIFO queue; complete and optimal for equal step costs"),
           ("DFS", "Uses a LIFO stack; memory grows only linearly with depth"),
           ("Iterative deepening", "Repeated depth-limited DFS with an increasing limit"),
           ("A*", "Orders nodes by f(n) = g(n) + h(n)")])

# ----------------------------------------------------------------------------
# CONSTRAINT SATISFACTION PROBLEMS
# ----------------------------------------------------------------------------
add("MCQ", "Constraint Satisfaction Problems", "Easy",
    "A Constraint Satisfaction Problem (CSP) is defined by:",
    "Variables, domains, and constraints",
    "A CSP assigns values from each variable's domain such that all constraints are satisfied.",
    "Three ingredients starting with V, D and C.",
    options=["Variables, domains, and constraints",
             "States, actions, and path costs",
             "Percepts, actuators, and sensors",
             "Heuristics, goals, and operators"])

add("Scenario", "Constraint Satisfaction Problems", "Medium",
    "A university schedules exams so that no two exams that share students are held in the same time slot. "
    "How is this modelled as a CSP?",
    "Variables = exams; domains = time slots; constraints = exams sharing students cannot share a slot",
    "Each exam is a variable, the available slots form its domain, and a binary constraint forbids the same slot for exams with common students.",
    "What must be decided? From which values?",
    options=["Variables = exams; domains = time slots; constraints = exams sharing students cannot share a slot",
             "Variables = students; domains = exams; constraints = every student takes one exam",
             "Variables = time slots; domains = students; constraints = none",
             "Variables = rooms; domains = exams; constraints = rooms must be large"],
    real=True)

add("MCQ", "Constraint Satisfaction Problems", "Medium",
    "In backtracking search for CSPs, the Minimum Remaining Values (MRV) heuristic chooses:",
    "The variable with the fewest legal values left",
    "MRV ('fail-first') picks the most constrained variable, so dead ends are discovered early and the search tree stays small.",
    "Choose the most constrained variable first.",
    options=["The variable with the fewest legal values left", "The variable with the most legal values left",
             "A random value for every variable", "The value that appears most often in the domain"])

add("Problem Solving", "Constraint Satisfaction Problems", "Medium",
    "Three regions A, B and C are all mutually adjacent (a triangle). Using 3 colours so that adjacent regions differ, how many valid colourings exist?",
    "6",
    "A has 3 choices, B has 2 (not A's colour), C has 1 (neither A's nor B's colour): 3 x 2 x 1 = 6.",
    "Multiply the remaining choices for each region in turn.",
    options=["3", "6", "9", "27"],
    search=True)

add("Problem Solving", "Constraint Satisfaction Problems", "Hard",
    "How many distinct solutions does the 4-Queens problem have on a 4x4 board (no two queens attack each other)?",
    "2",
    "4-Queens has exactly 2 solutions (mirror images of each other): queens in columns (2, 4, 1, 3) and (3, 1, 4, 2).",
    "Each row has exactly one queen; the solutions are mirror images.",
    options=["1", "2", "4", "8"],
    search=True)

# ----------------------------------------------------------------------------
# MEANS-END ANALYSIS
# ----------------------------------------------------------------------------
add("MCQ", "Means-End Analysis", "Medium",
    "In means-end analysis, if the operator chosen to reduce the biggest difference cannot be applied because its preconditions are not met, what is done?",
    "A sub-goal is created to satisfy the preconditions and MEA is applied recursively",
    "MEA breaks the problem into sub-problems: first achieve the operator's preconditions, then apply the operator, then continue toward the goal.",
    "Recursion on sub-goals.",
    options=["A sub-goal is created to satisfy the preconditions and MEA is applied recursively",
             "The search restarts from a random state",
             "The operator is applied anyway",
             "The goal state is modified"])

add("Scenario", "Means-End Analysis", "Hard",
    "A delivery drone must take a parcel across town. The operator 'Fly to destination' reduces the biggest difference (location) but needs battery >= 60%, and the battery is at 20%. "
    "What does means-end analysis do next?",
    "Set the sub-goal 'charge battery to >= 60%' and solve it first",
    "The unmet precondition becomes a new sub-goal. Once the drone is charged, the original operator can be applied.",
    "Unmet preconditions become sub-goals.",
    options=["Set the sub-goal 'charge battery to >= 60%' and solve it first",
             "Discard the Fly operator and restart from scratch",
             "Apply Fly anyway and hope the battery lasts",
             "Change the destination to somewhere nearer"],
    real=True)

add("Fill in the Blanks", "Means-End Analysis", "Medium",
    "Means-end analysis was a key technique of Newell and Simon's ________ ________ ________ (GPS) program.",
    "General Problem Solver",
    "GPS repeatedly picked the most significant difference between the current and goal state and selected an operator to reduce it.",
    "G in GPS stands for ...",
    accept=["general problem solver", "gps"])
