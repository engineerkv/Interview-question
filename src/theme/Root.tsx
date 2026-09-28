import type {ReactNode} from 'react';
import StudyChrome from '@site/src/components/StudyChrome';

export default function Root({children}: {children: ReactNode}): ReactNode {
  return (
    <>
      <StudyChrome />
      {children}
    </>
  );
}
