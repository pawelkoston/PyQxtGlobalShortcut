
class QxtGlobalShortcut : QObject
{

%TypeHeaderCode
#include "qxtglobalshortcut.h"
%End

public:
    explicit QxtGlobalShortcut(QObject* parent /TransferThis/ = 0);
    explicit QxtGlobalShortcut(const QKeySequence& shortcut, QObject* parent /TransferThis/ = 0);
    virtual ~QxtGlobalShortcut();
    QKeySequence shortcut() const;
    bool setShortcut(const QKeySequence& shortcut);
    bool isEnabled() const;

public slots:
    void setEnabled(bool enabled = true);
    void setDisabled(bool disabled = true);

signals:
    void activated();

};
