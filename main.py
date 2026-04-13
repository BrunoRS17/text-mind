import sys
from analyzer import TextMindAnalyzer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.theme import Theme

# Definindo um tema para o projeto
custom_theme = Theme({
    "info": "cyan",
    "warning": "yellow",
    "danger": "bold red",
    "success": "green",
    "title": "bold white on blue"
})

console = Console(theme=custom_theme)



def main():
    console.print(Panel.fit(" TEXTMIND - ANALISADOR INTELIGENTE ", style="title"))

    # Entrada de texto
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
    else:
        console.print("\n[info]Digite ou cole seu texto abaixo. [/info]")
        console.print("[dim](Para finalizar: Windows Enter + Ctrl+Z + Enter | Linux/Mac Ctrl+D)[/dim]\n")
        try:
            input_text = sys.stdin.read()
        except EOFError:
            input_text = ""

    if not input_text.strip():
        console.print("[danger]Erro: Nenhum texto fornecido para análise.[/danger]")
        return



    # Processamento junto com feedback visual
    with console.status("[bold green]Processando linguagem natural..."):
        analyzer = TextMindAnalyzer(input_text)
        stats = analyzer.get_basic_stats()
        sentiment = analyzer.get_sentiment()
        summary = analyzer.get_summary()



    # Tabela de Estatísticas
    table = Table(title="Métricas do Texto", title_style="bold magenta")
    table.add_column("Categoria", style="cyan")
    table.add_column("Resultado", style="white")

    table.add_row("Total de Palavras", str(stats['total_words']))
    table.add_row("Palavras Únicas", str(stats['unique_words']))
    table.add_row("Palavras-chave", ", ".join([w[0] for w in stats['top_words']]))
    table.add_row("Análise de Sentimento", sentiment.strip())

    console.print(table)



    # Painel de Resumo
    console.print(Panel(summary, title="[bold]RESUMO[/bold]", border_style="green", padding=(1, 2)))
    console.print("\n[dim]Análise finalizada com sucesso.[/dim]")




if __name__ == "__main__":
    main()